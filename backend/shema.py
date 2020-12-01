from pydantic import BaseModel 
from typing import Optional

class UserCreate(BaseModel):
    full_name: Optional[str] = None
    username : str
    password : str
    class Config:
        orm_mode = True

class User(UserCreate):
    id : int
    class Config:
        orm_mode = True

class ItemCreate(BaseModel):
    label : str
    price : float

class Item(ItemCreate):
    id : int
    userId : int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
