import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
COGNITO_CLIENT_ID=os.getenv("COGNITO_CLIENT_ID")
COGNITO_USER_POOL_ID=os.getenv("COGNITO_USER_POOL_ID")
COGNIT_REGION=os.getenv("COGNIT_REGION")
COGNIT_URL=os.getenv("COGNIT_URL")
COGNIT_JWK_URL=os.getenv("COGNIT_JWK_URL")
DB_URL=os.getenv("DB_URL")
