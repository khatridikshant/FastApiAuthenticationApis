import fastapi.routing as router
from fastapi.responses import JSONResponse
from fastapi import status,Depends
from sqlalchemy.orm import Session
from db import get_db
from user.schemas import CreateUserRequest
from user.services import create_user_account

_router = router.APIRouter(prefix="/users", tags=["User"],responses={404: {"description" : "Not Found"}})

@_router.post("",status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db:Session = Depends(get_db)):
    await create_user_account(data = data, db = db)
    payload = "User Account Has Been Successfully Created"
    return JSONResponse(content=payload)
