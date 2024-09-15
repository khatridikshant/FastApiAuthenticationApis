from fastapi import APIRouter, Depends
from fastapi import status
from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2PasswordRequestForm
from services import get_token

from db import get_db


router = APIRouter(prefix="/auth",tags=["Auth"],responses={404: {"description": "Not Found"}})

@router.post("/token",status_code=status.HTTP_200_OK)
async def authenticate_user(data: OAuth2PasswordRequestForm = Depends(), Session = Depends(get_db)):
    return await get_token(data,data)

