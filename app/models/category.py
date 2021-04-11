from datetime import datetime

from database import Base
from sqlalchemy import DATETIME, Column, Integer, String


class CategoryOrm(Base):
    __tablename__ = "CategoriesOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column("title", String(255), nullable=False)
    picture = Column("picture", String(255))
    like_sum = Column("like_sum", Integer, nullable=False)
    assumptions_like_sum = Column("asuumptions_like_sum", Integer, nullable=False)
    created = Column("created", DATETIME, default=datetime.now, nullable=False)
