from fastapi import APIRouter
from fastapi import status
from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth",tags=["Auth"],responses={404: {"description": "Not Found"}})

# @router.post("/token",status_code=status.HTTP_200_OK)
# async def authenticate_user(data):
