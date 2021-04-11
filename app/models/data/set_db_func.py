from typing import Dict, List

from article import ArticlesOrm
from assumpiont import AssumptionsOrm
from category import CategoriesOrm
from database import session
from follow import FollowsOrm
from like import LikesOrm
from request import RequestsOrm
from user import UsersOrm

category_map = {
    "mathmatics": 0,
    "physics": 1,
    "chemistory": 2,
    "biology": 3,
    "geosience": 4,
    "computer": 5,
}
request_which_map = {"category": 0, "assumption": 1, "App_request": 2}
like_which_map = {"category": 0, "assumption": 1, "article": 2}


def article_add_to_DB(data: List[Dict[str, str]]) -> None:
    new_article = ArticlesOrm(
        reply_to=-1,
        assumption_id=data[0]["assumption_id"],
        user_id=-1,
        title=data[1]["title"],
        coment=data[1]["coment"],
        like_sum=0,
    )

    if (
        ArticlesOrm.query.filter(
            ArticlesOrm.title == data[1]["title"]
            and ArticlesOrm.comment == data[1]["comment"]
        ).first()
        is None
    ):
        session.add(new_article)
        session.flush()
    return


def assumption_add_to_DB(category: str, data: str) -> None:
    new_assumption = AssumptionsOrm(
        category_id=category_map[category], title=data, like_sum=0, comments_like_sum=0
    )
    if AssumptionsOrm.filter(AssumptionsOrm.title == data).first() is None:
        session.add(new_assumption)
        session.flush()
    return


def request_add_to_DB(data: List[Dict[str, str]]) -> None:
    new_request = RequestsOrm(
        category_id=category_map[data[0]["category"]],
        title=data[1]["title"],
        user_id=-1,
        like_sum=0,
        request_which=request_which_map[data[0]["which"]],
    )
    session.add(new_request)
    session.flush()
    return


def category_add_to_DB(data: str) -> None:
    new_category = CategoriesOrm(
        title=data,
        like_sum=0,
        assumptions_like_sum=0,
    )
    if CategoriesOrm.filter(CategoriesOrm.title == data).first() is None:
        session.add(new_category)
        session.flush()
    return


def follow_add_to_DB(data: Dict[str, str]) -> None:
    new_follow = FollowsOrm(
        follow_id=data["follow_id"], follower_id=data["follower_id"]
    )
    if (
        FollowsOrm.filter(
            FollowsOrm.follow_id == data["follow_id"]
            and FollowsOrm.follower_id == data["follower_id"]
        ).first()
        is None
    ):
        session.add(new_follow)
        session.flush()
    else:
        session.delete(new_follow)
        session.flush()
    return


def like_add_to_DB(user_id: int, data: List[Dict[str, str]]) -> None:
    new_like = None
    if data[0]["like_which"] == "category":
        new_like = LikesOrm(
            like_which=like_which_map[data[0]["like_which"]],
            category_id=category_map[data[0]["object"]],
            title=data[1]["title"],
            user_id=user_id,
            like_sum=0,
        )
    elif data[0]["like_which"] == "assumption":
        new_like = LikesOrm(
            like_which=like_which_map[data[0]["like_which"]],
            assumption_id=data[0]["id"],
            title=data[1]["title"],
            user_id=user_id,
            like_sum=0,
        )
    elif data[0]["like_which"] == "article":
        new_like = LikesOrm(
            like_which=like_which_map[data[0]["like_which"]],
            article_id=data[0]["id"],
            title=data[1]["title"],
            user_id=user_id,
            like_sum=0,
        )
    if data[0]["like_which"] == "category":
        if (
            LikesOrm.filter(
                LikesOrm.user_id == user_id
                and LikesOrm.like_which == like_which_map[data[0]["like_which"]]
                and LikesOrm.category_id == data[0]["id"]
            ).first()
            is None
        ):
            session.add(new_like)
            session.flush()
        else:
            session.delete(new_like)
            session.flush()
    elif data[0]["like_which"] == "assumption":
        if (
            LikesOrm.filter(
                LikesOrm.user_id == user_id
                and LikesOrm.like_which == like_which_map[data[0]["like_which"]]
                and LikesOrm.assumption_id == data[0]["id"]
            ).first()
            is None
        ):
            session.add(new_like)
            session.flush()
        else:
            session.delete(new_like)
            session.flush()
    elif data[0]["like_which"] == "article":
        if (
            LikesOrm.filter(
                LikesOrm.user_id == user_id
                and LikesOrm.like_which == like_which_map[data[0]["like_which"]]
                and LikesOrm.object_id == data[0]["id"]
            ).first()
            is None
        ):
            session.add(new_like)
            session.flush()
        else:
            session.delete(new_like)
            session.flush()
    return


def user_add_to_DB(data: Dict[str, object]) -> None:
    new_user = UsersOrm(
        name=data["name"],
        like_sum=0,
        picture="assets/static/default-icon.png",
        profile=data["profile"],
    )
    # TODO
    session.add(new_user)
    session.flush()
    return
