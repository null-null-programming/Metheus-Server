from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from .env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

DATABASE = "mariadb://{user}:{password}@{host}/{db}?charset=utf8mb4".format(
    user=DB_USER, password=DB_PASSWORD, host=DB_HOST, db=DB_NAME)


ENGINE = create_engine(DATABASE)

session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
