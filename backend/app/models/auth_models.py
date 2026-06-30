from pydantic import BaseModel,EmailStr,Field

class RegisterRequest(BaseModel):
    email: EmailStr = Field(min_length=3,max_length=50)
    password: str = Field(min_length=6)
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    email: EmailStr


class UserResponse(BaseModel):
    email: EmailStr