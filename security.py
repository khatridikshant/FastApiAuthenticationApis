from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from argon2 import PasswordHasher

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


passwordhasher = PasswordHasher()
def get_password_hash(password):
    return passwordhasher.hash(password)

def verify_password(password,hashed_password):
    try:

        valuehash = passwordhasher.verify(hashed_password,password)

        if valuehash == True:
            return True
        else:
            return False
    
    except:
        return False
    
    




