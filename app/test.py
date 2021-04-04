import requests
import json

import jwt
from jwt.algorithms import RSAAlgorithm

id_token = "eyJraWQiOiIrVDJkVUduQTNYN1lueDBsdkIwblNLdkQyTG9ZRFI1SUcyeDVoUWJMQjUwPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxMGZhOWIxZC01MTNkLTQ2NjAtYjQ1OC1kNjk5MDIxZGEwZWYiLCJhdWQiOiIzbDlmOXEwcmQ3M3VjZzRocGcxaGJ0b3VzdiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJldmVudF9pZCI6IjUzNDhjMDFlLTg1YTMtNDZjNC1hODI5LWMyM2QyNzYwYjNlZSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjE3NDM0Mjc3LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl9sMWJHRjlHRWgiLCJjb2duaXRvOnVzZXJuYW1lIjoibnVsbF9udWxsIiwiZXhwIjoxNjE3NDM3ODc3LCJpYXQiOjE2MTc0MzQyNzcsImVtYWlsIjoibnVsbG51bGxwcm9ncmFtbWluZ0BnbWFpbC5jb20ifQ.Cu9hXI7lNmE7URK1660YeThbWP45hY3yimUbX97xD2Q4Cnn68sGw2unflPtgmhDh-1NXGVdpZKVZI1gVZHP0MczsErexJyLdDTz3ARNBOWhPkUyeoYsALTrKxG_p5H5H50nBCWxuSfbn4orHokc5fW0hpyvks-WefaeeiZaxNkhg4St-zy_S-E19njBwfUsT6fJhrpnaUsUakxyt65AewdH_zmyWY_upxRrQwcTdtXcRYMLX7SBMyRw3Nx3O8SKsx1HwLU030nt3cHs1wYt3pa50UpY7kQ1tMI2qa-_LjuAHQGStOPn0pbkAlwH3XWlxP12GZDDWz6zmlabJYxCShQ" # IDトークン
cognito_region = "4fqujurugia17d48c90n1cbf52"
cognito_client_id = "4fqujurugia17d48c90n1cbf52"
cognito_user_pool_id = "us-west-2_TjrcNQCxL"

cognito_url = (
    f"https://cognito-idp.us-west-2.amazonaws.com/us-west-2_TjrcNQCxL"
)
cognito_jwk_url = f"https://metheus.auth.us-west-2.amazoncognito.com/.well-known/jwks.json"

# TokenのヘッダからKey IDと署名アルゴリズムを取得
jwt_header = jwt.get_unverified_header(
    id_token
)  # -> {'alg': 'RS256', 'kid': 'xxxxxxxxxxxxx'}
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
# - 対象者 ( aud ) のクレームの検証
# - 発行者 ( iss ) のクレームの検証
json_payload = jwt.decode(
    id_token,
    public_key,
    algorithms=[jwt_algorithms],
    verify=True,
    options={"require_exp": True},
    audience=cognito_client_id,
    issuer=cognito_url,
)

# token_use クレームを検証（今回はIDトークンであることを確認）
if not "id" in json_payload["token_use"]:
    raise Exception("Not ID Token")

print(json.dumps(json_payload, indent=2))