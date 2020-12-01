from pydantic import BaseModel 
from typing import Optional

class User(BaseModel):
    id : int
    full_name: Optional[str] = None
    username : str
    password : str
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
