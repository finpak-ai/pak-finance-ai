from fastapi import APIRouter, Depends
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.db import database
from app.core.deps import get_current_user

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/", response_model=TransactionResponse)
def create_transaction(
    tx: TransactionCreate,
    user_email: str = Depends(get_current_user)
):
    conn = database.get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO transactions (user_email, amount, category, type) VALUES (?, ?, ?, ?)",
            (user_email, tx.amount, tx.category, tx.type)
        )
        conn.commit()
        tx_id = cursor.lastrowid
    finally:
        conn.close()

    return TransactionResponse(id=tx_id, **tx.dict())
