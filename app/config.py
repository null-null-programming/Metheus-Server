import os
from dotenv import load_dotenv

load_dotenv()

AUTH_CLIENT_DOMAIN = os.getenv('AUTH_CLIENT_DOMAIN')
AUTH_CLIENT_ID = os.getenv('AUTH_CLIENT_ID')
AUTH_CLIENT_SECRET = os.getenv('AUTH_CLIENT_SECRET')

DB_USER = os.getenv('MYSQL_USER')
DB_PASSWORD = os.getenv('MYSQL_PASSWORD')
DB_HOST = os.getenv('MYSQL_HOST')
DB_NAME = os.getenv('MYSQL_DATABASE')
