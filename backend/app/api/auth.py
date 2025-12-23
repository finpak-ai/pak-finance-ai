from fastapi import APIRouter
from app.schemas.user import UserRegister

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserRegister):
    return {
        "message": "User registered successfully",
        "email": user.email
    }
