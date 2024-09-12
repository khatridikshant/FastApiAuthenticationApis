from user.models import UserModel
from fastapi.exceptions import HTTPException
from security import get_password_hash
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db


async def create_user_account(data, db:Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == data.email).first()
    if user:
        raise HTTPException(status_code=442, detail="Email is already registered with us")
    
    new_user = UserModel(
    first_name = data.first_name,
    last_name = data.last_name,
    email = data.email,
    password = get_password_hash(data.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user