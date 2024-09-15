from fastapi import Depends
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from argon2 import PasswordHasher
import jwt
import starlette
import starlette.authentication
import starlette.middleware
import auth

from db import get_db
from user.models import UserModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


passwordhasher = PasswordHasher()
def get_password_hash(password):
    return passwordhasher.hash(password)

async def create_refresh_token(data):
    return jwt.encode()


def verify_password(password,hashed_password):
    try:

        valuehash = passwordhasher.verify(hashed_password,password)

        if valuehash == True:
            return True
        else:
            return False
    
    except:
        return False


def current_user(token:str = Depends(oauth2_scheme), db=None):
    payload = auth.services.get_token_payload(token)
    if not payload or type(payload) is not dict:
        return None
    
    user_id = payload.get('id', None)

    if not user_id:
        return None
    
    if not db:
        db = next(get_db())

    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    return user




class JWTAuth:
    async def authenticate(self, conn):
        guest = starlette.authentication.AuthCredentials(['unauthenticated']), starlette.authentication.UnauthenticatedUser()
        if 'authorization' not in conn.headers:
            return guest
        
        token = conn.headers.get('authorization').split(' ')[1] #Bearer token_hash
        if not token:
            return guest
        
        user = current_user(token)

        if not user:
            return guest
        
        return starlette.authentication.AuthCredentials('authenticated'), user

    
    
    




