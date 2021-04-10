from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from pydantic import BaseModel


class Article(BaseModel):
    __tablename__ = "Article"
    id: int
    assumption_id: int
    user_id: int
    title: str
    article: str
