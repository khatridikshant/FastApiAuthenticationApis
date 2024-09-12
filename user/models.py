from sqlalchemy import Boolean, Column, Integer, String, DateTime
from db import Base

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(250), unique=True, index=True)
    password = Column(String(100))

