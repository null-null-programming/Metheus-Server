from database import Base
from sqlalchemy import Column, Integer, String,DATETIME
from datetime import datetime


class AssumptionOrm(Base):
    __tablename__ = "AssumptionsOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    category_id = Column("category_id", Integer, nullable=False)
    title = Column("title", String(256), nullable=False)
    like_sum = Column("like_sum", Integer, nullable=False)
    comments_like_sum = Column("comments_like_sum", Integer, nullable=False)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
