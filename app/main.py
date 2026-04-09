from fastapi import FastAPI

from .routers import users
from .db.session import SessionLocal

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    return{"message":"Hello, World!"}