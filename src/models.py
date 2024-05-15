from settings import settings
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class Base(settings.BASE):
    pass


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    authors = relationship("Author", back_populates="articles", lazy="joined")
    author_id = Column(Integer, ForeignKey('authors.id'))
    

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    books = relationship("Book", back_populates="authors", lazy="joined")
    articles = relationship("Article", cascade="all,delete-orphan", back_populates="authors", uselist=True, lazy="joined")
