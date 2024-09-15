import fastapi.routing as router
from fastapi.responses import JSONResponse
from fastapi import HTTPException, Request, status,Depends
from sqlalchemy.orm import Session
from db import get_db
from user.models import UserJwt, UserModel
from user.schemas import CreateUserRequest
from user.services import create_user_account
from starlette.middleware.authentication import AuthenticationMiddleware
import security


_router = router.APIRouter(prefix="/users", tags=["User"],responses={404: {"description" : "Not Found"}})
_userrouter = router.APIRouter(prefix="/users", tags=["User"],responses={404: {"description" : "Not Found"}}, dependencies= [Depends(security.oauth2_scheme)])

@_router.post("")
async def create_user(data: CreateUserRequest, db:Session = Depends(get_db)):
    await create_user_account(data = data, db = db)
    payload = "User Account Has Been Successfully Created"
    return JSONResponse(content=payload)

@_router.get("/get/{id}")
async def get_users(id: int, db:Session = Depends(get_db)):
    db_item = db.query(UserModel).filter(UserModel.id == id).first()
    if db_item is None:
        raise HTTPException(status_code = 404, detail = "Item Not Found")
    return db_item


@_userrouter.post("/account", status_code = status.HTTP_200_OK,response_model=UserJwt)
def get_user_details(request: Request):
    return request.user


@_userrouter.get("/getall", status_code=status.HTTP_200_OK)
async def get_allusers(db: Session = Depends(get_db)):
     
    dbitems =  db.query(UserModel).all()
    listitems = []
    for values in dbitems:
        listitems.append({
            "User-Name": values.first_name + " " + values.last_name,
            "Email": values.email  
        })
    return listitems
        
    


    


