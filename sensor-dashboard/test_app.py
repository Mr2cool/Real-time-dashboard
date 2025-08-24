import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Sensor Dashboard" in response.text

def test_sse_endpoint():
    with client.stream("GET", "/sse") as response:
        assert response.status_code == 200
        # Read the first line of the SSE stream
        first_line = next(response.iter_lines())
        assert first_line.startswith(b"data:")