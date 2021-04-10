from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import ENGINE, Base


class FollowOrm(Base):
    __tablename__ = 'FollowOrm'
    id = Column('id', Integer, primary_key=True,
                autoincrement=True, nullable=False)
    follow_id = Column('follow_id', Integer, nullable=False)
    follower_id = Column('follower_id', Integer, nullable=False)
