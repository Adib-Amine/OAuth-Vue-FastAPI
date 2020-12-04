from fastapi.security import OAuth2PasswordBearer
from fastapi import  HTTPException, status
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "e505bf8963e5fd764c36f4f36d14af7c30e9f4f1b9851c9851b29f5043b82613"
# SECRET_KEY = "amine"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


#the OAuth2PasswordBearer class
#When we create an instance of the OAuth2PasswordBearer class we pass in the tokenUrl parameter
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

credentials_exception_admin = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You Are Not Authorized to Access This Page",
            headers={"WWW-Authenticate": "Bearer"},
        )
   
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

