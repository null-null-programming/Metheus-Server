import sys
from typing import Any, Dict, List, Optional

import auth_check as auth
from database import Base
from fastapi import FastAPI, Response
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from starlette.middleware.cors import CORSMiddleware


class Article(BaseModel):
    __tablename__ = "Article"
    assumption_id: int
    user_id: int
    title: str
    article: str


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
    # TODO create return_json by MariaDB
    return_json = [
        {"id": 0, "name": "Mathematics:数学"},
        {"id": 1, "name": "Physics:物理学"},
        {"id": 2, "name": "ComputerSicence:情報学"},
        {"id": 3, "name": "History:歴史"},
        {"id": 4, "name": "Biology:生物学"},
        {"id": 5, "name": "Chemistory:化学"},
    ]

    return return_json


@app.get("/category/{category_id}")
def get_assumptions(category_id: int) -> List[Dict[str, object]]:
    # TODO use MariaDB

    if category_id != 2:
        return [{}]

    # /category=computer-sienceの場合のデータ
    return_json = [
        {"id": 0, "category_id": 2, "user_id": 0, "title": "P!=NP"},
        {"id": 1, "category_id": 2, "user_id": 1, "title": "指数時間仮説"},
        {"id": 2, "category_id": 2, "user_id": 2, "title": "NPにおける不完全問題"},
        {"id": 3, "category_id": 2, "user_id": 3, "title": "一方向性関数の存在"},
        {"id": 4, "category_id": 2, "user_id": 4, "title": "計算機の速度限界"},
        {"id": 5, "category_id": 2, "user_id": 5, "title": "クラスターの参加ノード数限界"},
    ]

    return return_json


@app.get("/assumptions/{assumptions_id}")
def get_articles(assumptions_id: int) -> List[Dict[str, object]]:
    # TODO use MariaDB

    if assumptions_id != 0:
        return [{}]

    return_json = [
        {"id": 0, "assumptions_id": 0, "user_id": 0, "title": "暗号が壊れる"},
        {"id": 1, "assumptions_id": 1, "user_id": 1, "title": "Test"},
    ]

    return return_json


# TODO change post->put
# TODO setting auth
@app.post("/articles")
def post_article(article: Article) -> Dict[str, object]:
    # TODO MariaDB
    return {
        "assumption_id": article.assumption_id,
        "user_id": article.user_id,
        "title": article.title,
        "article": article.article,
    }


@app.put("/articles")
def put_article(article: Article, responce: Response) -> None:
    # TODO MariaDB
    print(responce["id_token"])  # type: ignore
    return
