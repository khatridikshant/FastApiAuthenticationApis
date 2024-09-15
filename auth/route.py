from fastapi import APIRouter, Depends, Header
from fastapi import status
from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2PasswordRequestForm
import sqlalchemy.orm
from auth.services import get_refresh_token, get_token
import sqlalchemy
from db import get_db


router = APIRouter(prefix="/auth",tags=["Auth"],responses={404: {"description": "Not Found"}})

@router.post("/token",status_code=status.HTTP_200_OK)
async def authenticate_user(data: OAuth2PasswordRequestForm = Depends(), db: sqlalchemy.orm.Session = Depends(get_db)):
    return await get_token(data,db)


@router.post("/refresh",status_code=status.HTTP_200_OK)
async def refresh_access_token(refresh_token: str = Header(), db: sqlalchemy.orm.Session = Depends(get_db)):
    return await get_refresh_token(refresh_token,db)


