import os
from dotenv import load_dotenv

load_dotenv()

AUTH_DOMAIN = os.getenv('AUTH_DOMAIN')
AUTH_CLIENT_ID = os.getenv('AUTH_CLIENT_ID')
AUTH_CLIENT_SECRET = os.getenv('AUTH_CLIENT_SECRET')
MACHINE_AUTH_CLIENT_ID = os.getenv('MACHINE_AUTH_CLIENT_ID')
MACHINE_AUTH_CLIENT_SECRET = os.getenv('MACHINE_AUTH_CLIENT_SECRET')
