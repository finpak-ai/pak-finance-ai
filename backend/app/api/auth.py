from sqlite3.dbapi2 import Cursor
from fastapi import APIRouter, HTTPException
from app.schemas.user import UserRegister, UserResponse
from app.core import security
from app.db import database

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserRegister):
    conn = database.get_conncetion()
    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email = ?", (user.email,))
    existing_user = cursor.fetchone()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash password
    hashed_password = security.hash_password(user.password)

    # Insert user
    cursor.execute(
        "INSERT INTO users (email, password) VALUES (?, ?)",
        (user.email, hashed_password)
    )
    conn.commit()

    user_id = cursor.lastrowid
    conn.close()


    return UserResponse(id=user_id, email=user.email)
