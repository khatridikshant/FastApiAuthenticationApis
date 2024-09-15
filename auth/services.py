import fastapi
from fastapi import Depends, HTTPException
import sqlalchemy
import sqlalchemy.orm
from auth.response import TokenResponse
from db import  get_db
from user.models import UserModel
from fastapi.security import OAuth2PasswordRequestForm
import security
import datetime
import jwt
from auth import samplejwtkeygenerator


async def get_token(data: OAuth2PasswordRequestForm, db: sqlalchemy.orm.Session ):
    user = db.query(UserModel).filter(UserModel.email == data.username).first()
    if user is None:
        raise HTTPException(status_code=400,detail="Not Registerd Email")


    if not security.verify_password(data.password,user.password):
         raise HTTPException(status_code=400,detail="Invalid Login Credentials")
    
    return await get_user_token(user=user)








async def create_access_token(payload: dict, exp: datetime.timedelta):
    payload = payload.copy()
    tokenTime = datetime.datetime.now().second + exp
    payload["time"] = tokenTime

    for key,value in payload.items():
        if isinstance(value, datetime.datetime):
            payload[key] = str(value) 
    token = jwt.encode(payload=payload,key = samplejwtkeygenerator.secretkey, algorithm= 'HS256')
    return token


async def create_refresh_token(data: dict):
    return jwt.encode(data,samplejwtkeygenerator.secretkey,"HS256")

async def get_user_token(user: UserModel, refresh_token = None):
    payload = {"id": user.id}
    access_token =  await create_access_token(payload,datetime.timedelta(minutes=60).seconds)
    if not refresh_token:
        refresh_token = await create_refresh_token(payload)
    return TokenResponse(access_token=access_token,refresh_token=refresh_token,expires_in=datetime.timedelta(minutes=60).seconds)


