from pydantic import BaseModel 
from typing import Optional


class User(BaseModel):
    id  : int
    username : str
    password : str
    type : str
    class Config:
        orm_mode = True

class Admin(User):
    id : int
    class Config:
        orm_mode = True

class Client(User):
    id : int
    full_name: Optional[str] = None
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

# class TokenData(BaseModel):
#     username: Optional[str] = None


    
# class Admin(BaseModel):
#     id  : int
#     username : str
#     password : str
#     class Config:
#         orm_mode = True

# class UserCreate(BaseModel):
#     full_name: Optional[str] = None
#     username : str
#     password : str
#     class Config:
#         orm_mode = True

# class User(UserCreate):
#     id : int
#     class Config:
#         orm_mode = True