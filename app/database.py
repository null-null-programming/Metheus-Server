import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv()
ENGINE = create_engine(os.getenv("DB_URL"))

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))
Base = declarative_base()
Base.query = Session.query_property()


def get_db() -> Generator:
    try:
        db = Session()
        yield db
    finally:
        db.close()
