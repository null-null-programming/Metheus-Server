from pydantic import BaseModel


class ArticleModel(BaseModel):
    __tablename__ = "ArticleModel"
    id: int
    assumption_id: int
    user_id: int
    title: str
    article: str
