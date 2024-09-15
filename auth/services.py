import fastapi
from fastapi import Depends, HTTPException
import sqlalchemy
import sqlalchemy.orm
from db import  get_db
from user.models import UserModel
from fastapi.security import OAuth2PasswordRequestForm
import security



async def get_token(data: OAuth2PasswordRequestForm, db: sqlalchemy.orm.Session ):
    user = db.query(UserModel).filter(UserModel.email == data.username).first()
    if user is None:
        raise HTTPException(status_code=400,detail="Not Registerd Email")


    if not security.verify_password(data.password,user.password):
         raise HTTPException(status_code=400,detail="Invalid Login Credentials")

