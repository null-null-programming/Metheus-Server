from datetime import datetime

from database import Base
from sqlalchemy import DATETIME, Column, Integer, String


class LikeOrm(Base):
    __tablename__ = "LikeOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    object_id = Column("category_id", Integer, nullable=False)
    title = Column("title", String(255), nullable=False)
    user_id = Column("user_id", Integer, nullable=False)
    like_sum = Column("email", Integer, nullable=False)
    like_which = Column("like_which", Integer, nullable=False)
    created = Column("created", DATETIME, default=datetime.now, nullable=False)
