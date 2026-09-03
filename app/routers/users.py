from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import *
from app.models import User
from app.services.security import hash_password
from app.services.security import verify_password

router = APIRouter()

@router.get("/test")
async def test():
    return{"messase": "user router works"}
    
@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists"
        )
        
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
        if verify_password(user.password, user_check.password):
            return {"message": "login successful"}
        else:
            return{"message": "invalid password"}
    else:
        return{"message": "user not found"}
    