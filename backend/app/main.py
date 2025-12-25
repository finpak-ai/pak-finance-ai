from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.transactions import router as transactions_router

app = FastAPI(title="Finance App API")

# Include routers
app.include_router(auth_router)
app.include_router(transactions_router)
