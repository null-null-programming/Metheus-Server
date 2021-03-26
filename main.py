from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import Column, Integer, String
from app.database import Base


class Article(Base):
    __tablename__ = "Article"

    id = Column(Integer, primary_key=True, index=True)
    assumption_id = Column(Integer, index=True)
    user_id = Column(Integer)
    title = Column(String(64))
    article = Column(String(4096))


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
            "id": 0, "name": "Mathmatics"
        }, {
            "id": 1, "name": "Physics"
        }, {
            "id": 2, "name": "ComputerSicence"
        }, {
            "id": 3, "name": "History"
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


@app.put("/articles")
def post_article():
    return {"name": "null_null"}
