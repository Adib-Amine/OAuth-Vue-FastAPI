from operator import mod
from fastapi import Depends, FastAPI ,Request, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from shema import User ,Token, TokenData,Item
from db import engine,SessionLocal
from sqlalchemy.orm import Session
import uvicorn
import models
import auth



app = FastAPI(debug=True)
#create db
models.Base.metadata.create_all(bind=engine)
#middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
#connect to db
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency
def get_db(request: Request):
    return request.state.db


# get_current_user will receive a token as a str from the sub-dependency oauth2_scheme
# will use a utility function we created,
# that takes a token as a str and returns our Pydantic User model:
async def get_current_user(token: str = Depends(auth.oauth2_scheme),db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise auth.credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise auth.credentials_exception
    user = auth.get_user(db=db, username=token_data.username)
    if user is None:
        raise auth.credentials_exception
    return user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise auth.credentials_exception
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=auth.access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/user/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    #We want to get the current_user .
    return current_user

@app.get("/user/items")
async def get_items_user(current_user : User = Depends(get_current_user),db: Session = Depends(get_db)):
    return db.query(models.Item).filter(models.Item.userId == current_user.id).all()


@app.get('/users')
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port='8000')

