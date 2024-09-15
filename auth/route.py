from fastapi import APIRouter, Depends
from fastapi import status
from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2PasswordRequestForm
import sqlalchemy.orm
from auth.services import get_token
import sqlalchemy
from db import get_db


router = APIRouter(prefix="/auth",tags=["Auth"],responses={404: {"description": "Not Found"}})

@router.post("/token",status_code=status.HTTP_200_OK)
async def authenticate_user(data: OAuth2PasswordRequestForm = Depends(), db: sqlalchemy.orm.Session = Depends(get_db)):
    return await get_token(data,db)

