from database import Base
from sqlalchemy import Column, Integer


class FollowOrm(Base):
    __tablename__ = "FollowOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    follow_id = Column("follow_id", Integer, nullable=False)
    follower_id = Column("follower_id", Integer, nullable=False)
