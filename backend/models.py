from sqlalchemy import Column, Integer, String
from db import Base 


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, index=True,autoincrement=True)
    full_name = Column(String(30))
    username = Column(String(20), index=True)
    password = Column(String(60))
