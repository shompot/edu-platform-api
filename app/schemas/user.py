from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class UserCreate (BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    
class UserLogin (BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
