
import os
from pathlib import Path
from fastapi import FastAPI

app = FastAPI(
    title="FinPilot AI",
    description="A personal finance assistant API - Secret Manager test",
    version="0.1.0",
)

expenses = [
    {"category": "Groceries", "amount": 450},
    {"category": "Transport", "amount": 200},
    {"category": "Utilities", "amount": 350},
]


@app.get("/")
def home():
    message = os.getenv("APP_MESSAGE", "Welcome to FinPilot Ai!")
    return {"message": message}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/expenses")
def get_expenses():
    total = sum(item["amount"] for item in expenses)
    return {
        "currency": "AED",
        "expenses": expenses,
        "total_expenses": total,
    }


@app.get("/secret-check")
def secret_check():
    secret_path = Path("/secrets/db-password")

    if not secret_path.is_file():
        return {
            "status": "failed",
            "message": "Secret file not found",
        }

    secret_value = secret_path.read_text().strip()

    if not secret_value:
        return {
            "status": "failed",
            "message": "Secret file is empty",
        }

    return {
        "status": "success",
        "message": "Secret Manager mounted volume is working!",
        "secret_loaded": True,
    }
