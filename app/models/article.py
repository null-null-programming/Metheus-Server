from pydantic import BaseModel


class Article(BaseModel):
    __tablename__ = "Article"
    id: int
    assumption_id: int
    user_id: int
    title: str
    article: str
