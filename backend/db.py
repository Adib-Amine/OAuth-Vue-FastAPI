from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL ="mysql+pymysql://b355fbf4790d03:181ec165@us-cdbr-east-02.cleardb.com/heroku_94c3a27a9b0dffd"
SQLALCHEMY_DATABASE_URL ="mysql+pymysql://root:@127.0.0.1/users"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()




# fake_users_db = {
#     # "johndoe": {
#     #     "username": "johndoe",
#     #     "full_name": "John Doe",
#     #     "email": "johndoe@example.com",
#     #     "hashed_password": "fakehashedsecret",
#     #     "disabled": False,
#     # },
#     # "alice": {
#     #     "username": "alice",
#     #     "full_name": "Alice Wonderson",
#     #     "email": "alice@example.com",
#     #     "hashed_password": "fakehashedsecret2",
#     #     "disabled": True,
#     # },
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     }
# }