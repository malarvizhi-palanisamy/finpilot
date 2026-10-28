import os
from fastapi import FastAPI

app = FastAPI(
    title="FinPilot AI",
    description="A personal finance assistant API",
    version="0.1.0",
)

# Sample data for our first version
expenses = [
    {"category": "Groceries", "amount": 450},
    {"category": "Transport", "amount": 200},
    {"category": "Utilities", "amount": 350},
]


@app.get("/")
def home():
    message = os.getenv("APP_MESSAGE", "Welcome to FinPilot AI!")
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
