from article import ArticlesOrm
from assumpiont import AssumptionsOrm
from category import CategoiesOrm
from follow import FollowsOrm
from like import LikesOrm
from request import RequestsOrm
from typing import Dict, List
from database import session

def articke_add_to_DB(data : Dict[str, object]) -> None:
    new_article=ArticlesORM(reply_to=data["reply_to"],assumptions=data["assumptions"],user_id=data["user_id"],title=data["title"],coment=data["coment"],like_sum=data["like_sum"])
    article_set=set()
    session.query(Article).all()