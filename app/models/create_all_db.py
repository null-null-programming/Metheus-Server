from datetime import datetime

from database import ENGINE, Base
from sqlalchemy import DATETIME, TEXT, Column, Integer, String


class ArticleOrm(Base):
    __tablename__ = "ArticlesOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    reply_to = Column("reply_to", Integer, nullable=False)
    assumption_id = Column("assumption_id", Integer, nullable=False)
    user_id = Column("user_id", Integer, nullable=False)
    title = Column("title", String(255), nullable=False)
    comment = Column("comment", TEXT(16380), nullable=False)
    like_sum = Column("like_sum", Integer, nullable=False)
    created = Column("created", DATETIME, default=datetime.now, nullable=False)


class AssumptionOrm(Base):
    __tablename__ = "AssumptionsOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    category_id = Column("category_id", Integer, nullable=False)
    title = Column("title", String(256), nullable=False)
    like_sum = Column("like_sum", Integer, nullable=False)
    comments_like_sum = Column("comments_like_sum", Integer, nullable=False)
    created = Column("created", DATETIME, default=datetime.now, nullable=False)


class CategoryOrm(Base):
    __tablename__ = "CategoriesOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column("title", String(255), nullable=False)
    picture = Column("picture", String(255))
    like_sum = Column("like_sum", Integer, nullable=False)
    assumptions_like_sum = Column("asuumptions_like_sum", Integer, nullable=False)
    created = Column("created", DATETIME, default=datetime.now, nullable=False)


class FollowOrm(Base):
    __tablename__ = "FollowOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    follow_id = Column("follow_id", Integer, nullable=False)
    follower_id = Column("follower_id", Integer, nullable=False)
    created = Column("created", DATETIME, default=datetime.now, nullable=False)


class LikeOrm(Base):
    __tablename__ = "LikesOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    object_id = Column("category_id", Integer, nullable=False)
    title = Column("title", String(255), nullable=False)
    user_id = Column("user_id", Integer, nullable=False)
    like_sum = Column("email", Integer, nullable=False)
    like_which = Column("like_whitch", Integer, nullable=False)
    created = Column("created", DATETIME, default=datetime.now, nullable=False)


class RequestOrm(Base):
    __tablename__ = "RequestsOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    category_id = Column("category_id", Integer, nullable=False)
    title = Column("title", String(256), nullable=False)
    user_id = Column("user_id", Integer, nullable=False)
    like_sum = Column("like_sum", Integer, nullable=False)
    which = Column("which", Integer, nullable=False)
    created = Column("created", DATETIME, default=datetime.now, nullable=False)


class UserORM(Base):
    __tablename__ = "UsersOrm"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column("name", String(256), nullable=False)
    picture = Column("picture", String(256), nullable=False)
    like_sum = Column("like_sum", Integer, nullable=False)
    profile = Column("profile", TEXT(16380))
    created = Column("created", DATETIME, default=datetime.now, nullable=False)


def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
