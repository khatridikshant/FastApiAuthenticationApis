import fastapi
from fastapi import Depends, HTTPException
import sqlalchemy
import sqlalchemy.orm
from db import  get_db
from user.models import UserModel
from fastapi.security import OAuth2PasswordRequestForm
import security
import datetime
import jwt
import samplejwtkeygenerator


async def get_token(data: OAuth2PasswordRequestForm, db: sqlalchemy.orm.Session ):
    user = db.query(UserModel).filter(UserModel.email == data.username).first()
    if user is None:
        raise HTTPException(status_code=400,detail="Not Registerd Email")


    if not security.verify_password(data.password,user.password):
         raise HTTPException(status_code=400,detail="Invalid Login Credentials")
    
    return '' # Return Access and Refresh Tokens






secret_key = samplejwtkeygenerator.generatejwtkey()


async def create_access_token(payload: dict, exp: datetime.timedelta):
    payload = payload.copy()
    tokenTime = datetime.datetime.now() + exp
    payload.update({"time": tokenTime})
    token = jwt.encode(payload=payload,key = secret_key, algorithm= ['HS256'] )
    return token


async def create_refresh_token(data: dict):
    return jwt.encode(data,secret_key,["HS256"])

def get_user_token(user: UserModel, refresh_token = None):
    payload = {"id": user.id, "timeNow": datetime.datetime.now()}
    access_token = create_access_token(payload,datetime.timedelta(minutes=10))
    if not refresh_token:
        refresh_token = create_refresh_token(payload)
    return ''


