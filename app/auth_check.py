import os
import dotenv
import requests
import json
import config
import jwt
from jwt.algorithms import RSAAlgorithm

cognito_region =config.COGNIT_REGION
cognito_client_id = config.COGNITO_CLIENT_ID
cognito_user_pool_id = config.COGNITO_USER_POOL_ID

cognito_url = config.COGNIT_URL
cognito_jwk_url = config.COGNIT_JWK_URL



def token_info(id_token):
    # TokenのヘッダからKey IDと署名アルゴリズムを取得
    jwt_header = jwt.get_unverified_header(id_token)  # -> {'alg': 'RS256', 'kid': 'xxxxxxxxxxxxx'}
    key_id = jwt_header["kid"]
    jwt_algorithms = jwt_header["alg"]

    # ヘッダから取得したKey IDを使い、署名検証用の公開鍵をCognitoから取得
    # 鍵は複数存在するので、ヘッダから取得したKey IDと合致するものを取得
    res_cognito = requests.get(cognito_jwk_url)

    jwk = None
    for key in json.loads(res_cognito.text)["keys"]:
        if key["kid"] == key_id:
            jwk = key
    if not jwk:
        raise Exception("JWK Not Found")
    public_key = RSAAlgorithm.from_jwk(json.dumps(jwk))

    # PyJWTではdecode時に様々な検証を行うことが可能
    # ここでは以下の検証を一気に行えます
    # - 署名を検証
    # - 有効期限( exp ), 発行時刻 ( iat )のクレームを検証
    # - 対象者 ( aud ) のクレームの検証c
    # - 発行者 ( iss ) のクレームの検証
    
    json_payload=None
    
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
    if not "id" in json_payload["token_use"]:
        raise Exception("Not ID Token")
    
    return json_payload