from fastapi.testclient import TestClient
from src.main import app, get_model
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True) 
def mock_model(monkeypatch):
    from src.model import create_model
    mock = create_model()
    monkeypatch.setattr("src.main.get_model", lambda: mock)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_model_loading():
    # Call the function that handles the logic
    model = get_model() 
    assert model is not None