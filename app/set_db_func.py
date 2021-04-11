from typing import Dict

from create_all_db import (ArticlesOrm, AssumptionsOrm, CategoriesOrm,
                           FollowOrm, LikesOrm, RequestsOrm, UsersOrm)
from models.database import session

category_map = {
    "mathmatics": 1,
    "physics": 2,
    "chemistory": 3,
    "biology": 4,
    "computer": 5,
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
        session.query(ArticlesOrm)
        .filter(
            ArticlesOrm.title == data["title"]
            and ArticlesOrm.comment == data["comment"]
        )
        .first()
        is None
    ):
        session.add(new_article)
        session.commit()
    return


def assumption_add_to_DB(data: Dict) -> None:
    new_assumption = AssumptionsOrm(
        category_id=category_map[data["category"]],
        title=data["title"],
        like_sum=0,
        comments_like_sum=0,
    )
    print(new_assumption.category_id, new_assumption.title)
    if (
        session.query(AssumptionsOrm)
        .filter(AssumptionsOrm.title == data["title"])
        .first()
        is None
    ):
        session.add(new_assumption)
        session.commit()
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
        session.commit()
    elif data["request_which"] == "assumption":
        new_request = RequestsOrm(
            category_id=data["id"],
            title=data["title"],
            user_id=-1,
            like_sum=0,
            request_which=request_which_map[data["request_which"]],
        )
        session.add(new_request)
        session.commit()
    return


def category_add_to_DB(data: str) -> None:
    new_category = CategoriesOrm(
        title=data,
        like_sum=0,
        assumptions_like_sum=0,
    )
    if session.query(CategoriesOrm).filter(CategoriesOrm.title == data).first() is None:
        session.add(new_category)
        session.commit()
    return


def follow_add_to_DB(data: Dict) -> None:
    new_follow = FollowOrm(follow_id=data["follow_id"], follower_id=data["follower_id"])
    if (
        session.query(FollowOrm)
        .filter(
            FollowOrm.follow_id == data["follow_id"]
            and FollowOrm.follower_id == data["follower_id"]
        )
        .first()
        is None
    ):
        session.add(new_follow)
        session.commit()
    else:
        session.delete(new_follow)
        session.commit()
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
            session.query(LikesOrm)
            .filter(
                LikesOrm.user_id == data["user_id"]
                and LikesOrm.like_which == like_which_map[data["like_which"]]
                and LikesOrm.assumption_id == data["id"]
            )
            .first()
            is None
        ):
            session.add(new_like)
            session.commit()
        else:
            session.delete(new_like)
            session.commit()
    elif data["like_which"] == "assumption":
        if (
            session.query(LikesOrm)
            .filter(
                LikesOrm.user_id == data["user_id"]
                and LikesOrm.like_which == like_which_map[data["like_which"]]
                and LikesOrm.assumption_id == data["id"]
            )
            .first()
            is None
        ):
            session.add(new_like)
            session.commit()
        else:
            session.delete(new_like)
            session.commit()
    elif data["like_which"] == "article":
        if (
            session.query(LikesOrm)
            .filter(
                LikesOrm.user_id == data["user_id"]
                and LikesOrm.like_which == like_which_map[data["like_which"]]
                and LikesOrm.object_id == data["id"]
            )
            .first()
            is None
        ):
            session.add(new_like)
            session.commit()
        else:
            session.delete(new_like)
            session.commit()
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
    session.commit()
    return
