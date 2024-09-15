from fastapi import FastAPI
from fastapi.responses import JSONResponse
import starlette
import starlette.middleware
import starlette.middleware.authentication
import auth.route
from security import JWTAuth
from user.routes import _router as user_router
import db
from user.models import UserModel
import auth
import auth.services



app = FastAPI()

db.Base.metadata.create_all(bind=db.engine)
app.include_router(user_router)
app.include_router(auth.route.router)
app.add_middleware(starlette.middleware.authentication.AuthenticationMiddleware, backend = JWTAuth())


@app.get("/")
def health_check():
    return JSONResponse(content={"status": "Running"})

