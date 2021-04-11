from typing import Generator

from config import DB_URL
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

a = "123"

load_dotenv()

ENGINE = create_engine(DB_URL)

SessionClass = sessionmaker(ENGINE)
Session = SessionClass()

Base = declarative_base()
Base.query = Session.query_property()


def get_db() -> Generator:
    try:
        db = Session()
        yield db
    finally:
        db.close()
    return
