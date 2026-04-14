from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from typing import List

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(10), Unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(30), Unique=True, nullable=False)

    posts: Mapped[List["Post"]] = relationship(backpopulates="authors")
