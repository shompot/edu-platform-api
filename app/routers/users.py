from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate
from app.schemas.user import UserLogin
from app.schemas.user import UserResponse
from app.models import User
from app.services.security import hash_password
from app.services.security import verify_password

router = APIRouter()

@router.post(
    "/register", 
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
    )
async def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists"
        )
        
    new_user = User(
        email=user.email,
        password=hash_password(user.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    user_check = db.query(User).filter(User.email == user.email).first()
    if not user_check:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    if not verify_password(user.password, user_check.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )    

    return{"message": "Login successful"}
    