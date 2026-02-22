from fastapi.testclient import TestClient
from src.main import app, model

# Create the client
client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_model_loading():
    assert model is not None