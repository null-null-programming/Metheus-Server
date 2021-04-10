from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import Column, Integer, String
from starlette.middleware.cors import CORSMiddleware
import jwt
import auth_check as auth
from models.database import Base
from models.article import ArticleOrm, ArticleModel
from models.like import LikeOrm
from models.category import CategoryOrm
from models.assumption import AssumptionOrm
from models.request import RequestOrm
from models.user import UserORM
from models.follow import FollowOrm


class FavData(BaseModel):
    flag: bool
    id: int


app = FastAPI()

# for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)


@app.get("/category")
def get_categories():
    # TODO create return_json by MariaDB
    return_json = [
        {
            "id": 0, "name": "Mathematics:数学"
        }, {
            "id": 1, "name": "Physics:物理学"
        }, {
            "id": 2, "name": "ComputerSicence:情報学"
        }, {
            "id": 3, "name": "History:歴史"
        }, {
            "id": 4, "name": "Biology:生物学"
        }, {
            "id": 5, "name": "Chemistory:化学"
        }
    ]

    return return_json


@app.get("/category/{category_id}")
def get_assumptions(category_id: int):
    # TODO use MariaDB

    if category_id != 2:
        return [{}]

    # /category=computer-sienceの場合のデータ
    return_json = [{
        "id": 0, "category_id": 2, "user_id": 0, "title": "P!=NP"
    }, {
        "id": 1, "category_id": 2, "user_id": 1, "title": "指数時間仮説"
    }, {
        "id": 2, "category_id": 2, "user_id": 2, "title": "NPにおける不完全問題"
    }, {
        "id": 3, "category_id": 2, "user_id": 3, "title": "一方向性関数の存在"
    }, {
        "id": 4, "category_id": 2, "user_id": 4, "title": "計算機の速度限界"
    }, {
        "id": 5, "category_id": 2, "user_id": 5, "title": "クラスターの参加ノード数限界"
    }
    ]

    return return_json


@app.get("/assumptions/{assumptions_id}")
def get_articles(assumptions_id: int):
    # TODO use MariaDB

    if assumptions_id != 0:
        return[{}]

    return_json = [{
        "id": 0, "assumptions_id": 0, "user_id": 0, "title": "暗号が壊れる"
    }, {
        "id": 1, "assumptions_id": 1, "user_id": 1, "title": "Test"
    }]

    return return_json


@app.get("/articles/{article_id}")
def get_article(article_id: int):
    if article_id != 0:
        return [{}]

    return_json = [{
        "title": "正規分布", "article": "\n  $f(x) = \\frac{1}{\\sqrt {2\\pi \\sigma^2}} \\exp\\Biggl(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\Biggr) \\qquad (-\\infty<x<\\infty)$"
    }]

    return return_json


# TODO setting auth
@app.post("/articles")
def post_article(article: ArticleModel):
    # TODO MariaDB
    return {"assumption_id": article.assumption_id, "user_id": article.user_id, "title": article.title, "article": article.article}


@app.put('/articles')
def post_article(article: ArticleModel, authorization: str = Header(...)):
    auth_info = auth.token_info(authorization)
    print(auth_info)
    # TODO MariaDB


@app.get('/like')
def get_fav_data(authorization: str = Header(...)):
    try:
        auth_info = auth.token_info(authorization)
        print(auth_info)
        # TODO mariadb
        return {"0": True, "1": False, "2": False, "3": True, "4": False, "5": True, "6": True, "7": False}
    except:
        return {}


@app.put('/like')
def put_fav_data(fav_data: FavData, authorization: str = Header(...)):
    try:
        auth_info = auth.token_info(authorization)
        print(auth_info)
        # TODO MariaDB
        print(fav_data.flag, fav_data.id)
    except:
        return {}
