from typing import Dict

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
    "computer": 4,
}
request_which_map = {"category": 0, "assumption": 1, "App_request": 2}
like_which_map = {"category": 0, "assumption": 1, "article": 2}


def new_article_add_to_DB(data: Dict) -> None:
    new_article = ArticlesOrm(
        reply_to=-1,
        assumption_id=data["assumption_id"],
        user_id=data["user_id"],
        title=data["title"],
        coment=data["coment"],
        like_sum=0,
    )

    if (
        ArticlesOrm.query.filter(
            ArticlesOrm.title == data["title"]
            and ArticlesOrm.comment == data["comment"]
        ).first()
        is None
    ):
        session.add(new_article)
        session.flush()
    return


def assumption_add_to_DB(data: Dict) -> None:
    new_assumption = AssumptionsOrm(
        category_id=category_map[data["category"]],
        title=data["title"],
        like_sum=0,
        comments_like_sum=0,
    )
    if AssumptionsOrm.filter(AssumptionsOrm.title == data["title"]).first() is None:
        session.add(new_assumption)
        session.flush()
    return


def request_add_to_DB(data: Dict) -> None:
    if data["request_which"] == "category":
        new_request = RequestsOrm(
            category_id=data["id"],
            title=data["title"],
            user_id=-1,
            like_sum=0,
            request_which=request_which_map[data["request_which"]],
        )
        session.add(new_request)
        session.flush()
    elif data["request_which"] == "assumption":
        new_request = RequestsOrm(
            category_id=data["id"],
            title=data["title"],
            user_id=-1,
            like_sum=0,
            request_which=request_which_map[data["request_which"]],
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


def follow_add_to_DB(data: Dict) -> None:
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


def like_add_to_DB(data: Dict) -> None:
    if data["like_which"] == "category":
        new_like = LikesOrm(
            like_which=like_which_map[data["like_which"]],
            category_id=data["id"],
            user_id=data["user_id"],
            like_sum=0,
        )
    elif data["like_which"] == "assumption":
        new_like = LikesOrm(
            like_which=like_which_map[data["like_which"]],
            assumption_id=data["id"],
            user_id=data["user_id"],
            like_sum=0,
        )
    elif data["like_which"] == "article":
        new_like = LikesOrm(
            like_which=like_which_map[data["like_which"]],
            article_id=data["id"],
            user_id=data["user_id"],
            like_sum=0,
        )
    if data["like_which"] == "category":
        if (
            LikesOrm.filter(
                LikesOrm.user_id == data["user_id"]
                and LikesOrm.like_which == like_which_map[data["like_which"]]
                and LikesOrm.assumption_id == data["id"]
            ).first()
            is None
        ):
            session.add(new_like)
            session.flush()
        else:
            session.delete(new_like)
            session.flush()
    elif data["like_which"] == "assumption":
        if (
            LikesOrm.filter(
                LikesOrm.user_id == data["user_id"]
                and LikesOrm.like_which == like_which_map[data["like_which"]]
                and LikesOrm.assumption_id == data["id"]
            ).first()
            is None
        ):
            session.add(new_like)
            session.flush()
        else:
            session.delete(new_like)
            session.flush()
    elif data["like_which"] == "article":
        if (
            LikesOrm.filter(
                LikesOrm.user_id == data["user_id"]
                and LikesOrm.like_which == like_which_map[data["like_which"]]
                and LikesOrm.object_id == data["id"]
            ).first()
            is None
        ):
            session.add(new_like)
            session.flush()
        else:
            session.delete(new_like)
            session.flush()
    return


def user_add_to_DB(data: Dict) -> None:
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
