from typing import Dict, List

from fastapi import FastAPI, Response
from models.article import ArticleModel
from models.create_all_db import (  # , FollowOrm, LikesOrm, RequestsOrm, UsersOrm
    ArticlesOrm,
    AssumptionsOrm,
    CategoriesOrm,
)

# from .models.set_db_func import new_article_add_to_DB
from models.database import session
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # 追記により追加
    allow_methods=["*"],  # 追記により追加
    allow_headers=["*"],  # 追記により追加
)


@app.get("/category")
def get_categories() -> List[Dict[str, object]]:
    return_json = []
    categories = session.query(CategoriesOrm).order_by(CategoriesOrm.like_sum).all()
    for category in categories:
        data = {"id": category.id, "name": category.title}
        return_json.append(data)
    print(return_json)
    return return_json


@app.get("/category/{category_id}")
def get_assumptions(category_id: int) -> List[Dict[str, object]]:
    print(category_id)
    return_json = []
    assumptions = (
        session.query(AssumptionsOrm)
        .filter(AssumptionsOrm.category_id + 1 == category_id)
        .all()
    )
    print(assumptions)
    for assumption in assumptions:
        data = {
            "id": assumption.id,
            "category_id": assumption.category_id,
            "like_sum": assumption.like_sum,
            "comments_like_sum": assumption.comments_like_sum,
            "title": assumption.title,
        }
        return_json.append(data)
    print(return_json)
    return return_json


@app.get("/assumptions/{assumptions_id}")
def get_articles(assumptions_id: int) -> List[Dict[str, object]]:
    return_json = []
    articles = session.query(ArticlesOrm).order_by(ArticlesOrm.created).all()
    for article in articles:
        data = {
            "id": article.id,
            "assumption_id": article.assumption_id,
            "user_id": article.user_id,
            "title": article.title,
        }
        return_json.append(data)
    print(return_json)
    return return_json


@app.get("/articles/{article_id}")
def get_article(article_id: int) -> List[Dict[str, object]]:
    return_json = []
    article = session.query(ArticlesOrm).order_by(ArticlesOrm.created).all()
    for art in article:
        data = {"title": art.title, "articke": art.article}
        return_json.append(data)
    print(return_json)
    return return_json


# TODO setting auth
@app.post("/articles")
def post_article(article: ArticleModel, responce: Response) -> None:
    print(responce)
    # new_article_add_to_DB({
    # "assumption_id": article.assumption_id,
    # "user_id": article.user_id,
    # "title": article.title,
    # "article": article.article,
    # })
    return


@app.put("/articles")
def put_article(article: ArticleModel, responce: Response) -> None:
    # TODO MariaDB
    print(responce["id_token"])  # type: ignore
    return
