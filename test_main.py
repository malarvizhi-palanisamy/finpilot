
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to FinPilot AI!"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_expenses():
    response = client.get("/expenses")
    data = response.json()

    assert response.status_code == 200
    assert data["currency"] == "AED"
    assert data["total_expenses"] == 1000
    assert len(data["expenses"]) == 3
