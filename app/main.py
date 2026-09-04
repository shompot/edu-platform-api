from fastapi import FastAPI

from app.routers import users
from app.db.session import engine
from app.db.base import Base
from app.models import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}