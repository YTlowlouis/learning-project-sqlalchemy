from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

engine = create_engine("sqlite:///database.db", echo=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)

    posts: = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id = mapped_column(ForeignKey("user.id"))
    author = relationship("User", back_populates="posts")

def init_db():
    Base.metadata.create_all(engine)

init_db()

Session = sessionmaker(bind=engine)
session = Session()

user = User(name="alice", email="alice@test.com")
user2 = User(name="bob", email="bob@test.com")

session.add(user)
session.add(user2)


session.commit()

users = select(User.name).where(User.name.in_(["alice", "bob"]))
for user in session.scalars(users):
    print(user)
