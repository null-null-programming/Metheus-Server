from database import Base
from sqlalchemy import Column, Integer, String,DATETIME
from datetime import datetime


class UserORM(Base):
    __tablename__ = "UserOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column("name", String(256), nullable=False)
    picture = Column("picture", String(256), nullable=False)
    like_sum = Column("like_sum", Integer, nullable=False)
    profile = Column("profile", String(16380))
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
