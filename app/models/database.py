<<<<<<< HEAD:app/models/database.py
=======
import os
from typing import Generator

>>>>>>> dev:app/database.py
from dotenv import load_dotenv
from config import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

<<<<<<< HEAD:app/models/database.py
ENGINE = create_engine(DB_URL)
=======
ENGINE = create_engine(os.getenv("DB_URL"))
>>>>>>> dev:app/database.py

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

Base = declarative_base()
Base.query = SessionLocal.query_property()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
    return
