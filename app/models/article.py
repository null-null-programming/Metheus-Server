from pydantic import BaseModel


class ArticleModel(BaseModel):
    __tablename__ = "ArticleModel"
    id: int
    assumption_id: int
    user_id: int
    title: str
    article: str


class ArticleOrm(Base):
    __tablename__ = 'ArticlesOrm'
    id = Column('id', Integer, primary_key=True,
                autoincrement=True, nullable=False)
    reply_to = Column('reply_to', Integer, nullable=False)
    assumption_id = Column('assumption_id', Integer, nullable=False)
    user_id = Column('user_id', Integer, nullable=False)
    title = Column('title', String(255), nullable=False)
    comment = Column('comment', TEXT(16380), nullable=False)
    like_sum = Column('like_sum', Integer, nullable=False)
