from fastapi import APIRouter
from app.schemas.user import UserCreate

router = APIRouter()

@router.get("/test")
async def test():
    return{"messase": "user router works"}
    
@router.post("/register")
async def register(user: UserCreate):
    return{"message": "user created"}
    