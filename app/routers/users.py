from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import *
from app.models import User
from app.services.security import hash_password

router = APIRouter()

@router.get("/test")
async def test():
    return{"messase": "user router works"}
    
@router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        email = user.email,
        password = hash_password(user.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    user_check = db.query(User).filter(User.email == user.email).first()
    if user_check:
        if user.password == user_check.password:
            return {"message": "login successful"}
        else:
            return{"message": "invalid password"}
    else:
        return{"message": "user not found"}
    