from fastapi import APIRouter, HTTPException
from app.schemas.user import UserRegister, UserResponse, UserLogin
from app.core import security
from app.db import database
from app.core.jwt import create_access_token


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserRegister):
    conn = database.get_connection()
    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email = ?", (user.email,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Email already registerd")

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

@router.post("/login")
def login(user: UserLogin):
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (user.email,))
    db_user = cursor.fetchone()
    conn.close()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not security.verify_password(user.password, db_user["password"]):
        raise HTTPException(status=401, detail="Invalid credintial")

    access_token = create_access_token({"sub": db_user["email"]})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

    from app.core.deps import get_current_user
    from fastapi import Depends

    @router.get("/me")
    def me(current_user: str = Depends(get_current_user)):
        return {"email": current_user}
