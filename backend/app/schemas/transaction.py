from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    category: str
    type: str  # income | expense

class TransactionResponse(TransactionCreate):
    id: int
