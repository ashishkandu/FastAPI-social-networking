from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    id: Optional[int] = None


class PostBase(BaseModel):
    # id: Optional[int] = randrange(4, 1000000)
    title: str
    content: str
    published: bool = True
    

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserBase

    class Config:
        from_attributes = True
        

class PostOut(BaseModel):
    Post: Post
    votes: int


class Vote(BaseModel):
    post_id: int
    dir: bool