from sqlalchemy import Column, Integer, String,ForeignKey,Float
from db import Base 
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, index=True,autoincrement=True)
    full_name = Column(String(30))
    username = Column(String(20), index=True)
    password = Column(String(60))
    subject = relationship("Item")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(30), index=True)
    price = Column(Float(3,3))
    userId  = Column(Integer, ForeignKey("users.id"))
