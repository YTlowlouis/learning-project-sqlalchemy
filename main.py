from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db", echo=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)

    #posts: Mapped[List["Post"]] = relationship(back_populates="author")

    #liked_post: Mapped[List["Post"]] = relationship("Post", se)

class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    #author = relationship("User", back_populates="name")

def init_db():
    Base.metadata.create_all(engine)

init_db()

Session = sessionmaker(bind=engine)
session = Session()

user = User(name="alice", email="alice@test.com")

session.add(user)
session.commit()

users = session.query(User).all()

for u in users:
    print(u.name)
