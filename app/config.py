import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
USER_POOL_ID=os.getenv("USER_POOL_ID")
APP_CLIENT_ID=os.getenv("APP_CLIENT_ID")
COGNITO_CLIENT_ID=os.getenv("COGNITO_CLIENT_ID")
COGNITO_USER_POOL_ID=os.getenv("COGNITO_USER_POOL_ID")


