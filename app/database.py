from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from env.py import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

DATABASE = "mysql://{user}:{password}@{host}/{db}?charset=utf8mb4".format(
    user=DB_USER, password=DB_PASSWORD, host=DB_HOST, db=DB_NAME)


engine = create_engine(
    DATABASE,
    encoding='utf8mb4',
    echo=True
)

Base = declarative_base()
Base.query = SessionLocal.query_property()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
