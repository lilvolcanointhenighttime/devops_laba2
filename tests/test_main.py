from fastapi.testclient import TestClient
import sys

from src.main import app

sys.path.append('../')
client = TestClient(app)

def test_space_formatting():
    response = client.get("/formatted-text")
    assert response.json() == "Hello, world."

