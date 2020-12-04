from sqlalchemy import Column, Integer, String,ForeignKey,Float
from db import Base 
from sqlalchemy.orm import relationship

# class Admin(Base):
#     __tablename__ = 'admin'
#     id = Column(Integer,primary_key=True, index=True,autoincrement=True)
#     username = Column(String(20), index=True)
#     password = Column(String(60))

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer,primary_key=True, index=True,autoincrement=True)
#     full_name = Column(String(30))
#     username = Column(String(20), index=True)
#     password = Column(String(60))
#     subject = relationship("Item")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(30), index=True)
    price = Column(Float(3,3))
    userId  = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, index=True,autoincrement=True)
    username = Column(String(20), index=True)
    password = Column(String(60))
    type = Column(String(20))  

class Admin(User):
    __tablename__ = 'admin'
    id = Column(ForeignKey("users.id"), primary_key=True)

class Client(User):
    __tablename__ = 'client'
    id = Column(ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(30))
    subject = relationship("Item")