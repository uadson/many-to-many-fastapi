from pydantic import BaseModel
from typing import Optional, List


class ArticleBase(BaseModel):
    title: str
    author_id: Optional[int]
    
    class Config:
        orm_mode = True


class Article(ArticleBase):
    id: Optional[int] = None
    

class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(BaseModel):
    title: Optional[str]
    
  
class ArticlePublic(BaseModel):
    id: int
    title: str
    
    
class ArticlesList(BaseModel):
    articles: List[ArticlePublic]