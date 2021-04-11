from database import Base
from sqlalchemy import Column, Integer, String,DATE
from datetime import datetime


class LikeOrm(Base):
    __tablename__ = "LikeOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    category_id = Column("category_id", Integer, nullable=False)
    title = Column("title", String(255), nullable=False)
    user_id = Column("user_id", Integer, nullable=False)
    like_sum = Column("email", Integer, nullable=False)
