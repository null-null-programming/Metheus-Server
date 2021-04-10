import json
from typing import Any, Dict, Optional

import config
import jwt
import requests
from jwt.algorithms import RSAAlgorithm

cognito_region = "us-west-2"
cognito_client_id = config.COGNITO_CLIENT_ID
cognito_user_pool_id = config.COGNITO_USER_POOL_ID
cognito_url = config.COGNITO_URL
cognito_jwk_url = config.COGNIT_JWK_URL


# TODO fix
def token_info(id_token: str) -> Optional[Dict[str, Any]]:  # type: ignore
    # TokenのヘッダからKey IDと署名アルゴリズムを取得
    # -> {'alg': 'RS256', 'kid': 'xxxxxxxxxxxxx'}
    # TODO fix
    jwt_header = jwt.get_unverified_header(id_token)  # type: ignore
    key_id = jwt_header["kid"]
    jwt_algorithms = jwt_header["alg"]

    # ヘッダから取得したKey IDを使い、署名検証用の公開鍵をCognitoから取得
    # 鍵は複数存在するので、ヘッダから取得したKey IDと合致するものを取得
    res_cognito = requests.get(cognito_jwk_url)

    print(res_cognito)

    jwk = None
    for key in json.loads(res_cognito.text)["keys"]:
        if key["kid"] == key_id:
            jwk = key
    if not jwk:
        raise Exception("JWK Not Found")
    # TODO fix
    public_key = RSAAlgorithm.from_jwk(json.dumps(jwk))  # type: ignore

    # PyJWTではdecode時に様々な検証を行うことが可能
    # ここでは以下の検証を一気に行えます
    # - 署名を検証
    # - 有効期限( exp ), 発行時刻 ( iat )のクレームを検証
    # - 対象者 ( aud ) のクレームの検証c
    # - 発行者 ( iss ) のクレームの検証

    json_payload = None

    try:
        json_payload = jwt.decode(
            id_token,
            public_key,
            algorithms=[jwt_algorithms],
            verify=True,
            options={"require_exp": True},
            audience=cognito_client_id,
            issuer=cognito_url,
        )
    except Exception as err:
        print(err)

    # token_use クレームを検証（今回はIDトークンであることを確認）
    # TODO fix
    if not ("id" in json_payload["token_use"]):  # type: ignore
        raise Exception("Not ID Token")

    return json_payload


id_token = "eyJraWQiOiJYODdsQ2paXC8xWXRHYk40TUJwd3hsVlhrbldRVGZiUlZMa1pORFZ3RG9iMD0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlY2NkZDgzNS1mMWY3LTQzYmEtODZhMi05OTVhZGE3MTg1YWQiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfRUpmRWRsS0o0IiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjpmYWxzZSwiY29nbml0bzp1c2VybmFtZSI6Im51bGxfbnVsbCIsImF1ZCI6IjI5aXFibHA0MnB2Zjg0cnFxbDZrMnRpMzZzIiwiZXZlbnRfaWQiOiJjZGQ4NWY0Yi1lZDU2LTQyNDYtYjg0ZS1jMWY2OGJjNmU1YzAiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTYxNzY3NjE4NCwicGhvbmVfbnVtYmVyIjoiKzgxMDkwOTE2MDM4NjkiLCJleHAiOjE2MTc2Nzk3ODQsImlhdCI6MTYxNzY3NjE4NCwiZW1haWwiOiJudWxsbnVsbHByb2dyYW1taW5nQGdtYWlsLmNvbSJ9.F6Ll1rOC_-Zf3pZOZhnMnyQZETL8BKvtQJXu8DBZxkO0g2QYc2NOpiAHXCQEFe8yku-Ha6xxXQZBt-qDr6j0mhJkg6Ey4Q5AOdXayxoxGnt4KYstHfjsBjjyydfje-MDhXiaxhGW502WwUfBuj7r0cfWbmwAYHeLX3YkclJe_o6SvzQpiXXx9HXIvUr6dMRCRC6PNFeUvdMZbaO_DDos2x1oQ_EZb2s-SepFt0GNXq1WMFB4bY1vskmf6Cw8xI64sj6ypP-2blSXf7yZH6aens_zadSdrvyFhLE9kToeKdF7-EGC13OZoa0FuqgEybFlN4tf5pvaINhgZ5M3Dxwv_w"
token_info(id_token)
