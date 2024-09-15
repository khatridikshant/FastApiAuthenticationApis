from fastapi import FastAPI
from fastapi.responses import JSONResponse
from user.routes import _router as user_router
import db
from user.models import UserModel
from auth.route import router as auth_router


app = FastAPI()

db.Base.metadata.create_all(bind=db.engine)
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
def health_check():
    return JSONResponse(content={"status": "Running"})

