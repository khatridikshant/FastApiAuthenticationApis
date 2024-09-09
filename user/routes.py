import fastapi.routing as router
from fastapi import status,Depends
from sqlalchemy.orm import Session

_router = router.APIRouter(prefix="/users", tags=["User"],responses={404: {"description" : "Not Found"}})

@_router.post("",status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db:Session = Depends(get_db)):
