import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv()
ENGINE = create_engine(os.getenv("DB_URL"))

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))
Base = declarative_base()
Base.query = session.query_property()


def get_db() -> Generator:
    try:
        db = session()
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    get_db()
