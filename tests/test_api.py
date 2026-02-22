from fastapi.testclient import TestClient
from src.main import app, get_model

# Create the client
client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_model_loading():
    model = get_model() 
    assert model is not None