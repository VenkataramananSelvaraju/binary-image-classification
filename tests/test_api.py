from fastapi.testclient import TestClient
from src.main import app
import pytest

client = TestClient(app)

# @pytest.fixture(autouse=True)
# def mock_model(monkeypatch):
#     from src.model import create_model
#     mock = create_model()
#     monkeypatch.setattr("src.main.model", mock)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_model_loading():
    # Verify model exists and is loaded
    from src.main import model
    assert model is not None