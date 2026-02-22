from fastapi.testclient import TestClient
from src.main import app, get_model
from src.model import create_model
import pytest

# Create the client
client = TestClient(app)

@pytest.fixture(autouse=True)
def override_model_dependency():
    mock = create_model()
    app.dependency_overrides[get_model] = lambda: mock
    yield  
    app.dependency_overrides.clear()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_model_loading():
    model = get_model() 
    assert model is not None