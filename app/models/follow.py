from datetime import datetime

from database import Base
from sqlalchemy import DATETIME, Column, Integer


class FollowOrm(Base):
    __tablename__ = "FollowsOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    follow_id = Column("follow_id", Integer, nullable=False)
    follower_id = Column("follower_id", Integer, nullable=False)
    created = Column("created", DATETIME, default=datetime.now, nullable=False)
