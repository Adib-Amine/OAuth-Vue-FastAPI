from operator import mod
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    user =  db.query(models.User).filter(models.User.username == username).first()
    if user.type == 'client':
        return db.query(models.Client).filter(models.Client.username == username).first()
    return user
    
def get_client(db,username:str):
    return db.query(models.User).join(models.Client).filter(models.User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if user is None:
        return False
    if not verify_password(password, user.password):
        return False
    return user

# def authenticate_admin(db: Session, username: str, password: str):
#     user = get_admin(db, username)
#     if user is None:
#         return False
#     if not verify_password(password, user.password):
#         return False
#     return user
