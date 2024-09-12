from fastapi import FastAPI
from fastapi.responses import JSONResponse
from user.routes import _router as user_router
import db
from user.models import UserModel


app = FastAPI()

db.Base.metadata.create_all(bind=db.engine)
app.include_router(user_router)

@app.get("/")
def health_check():
    return JSONResponse(content={"status": "Running"})

