"""Tests for GET requests in the FastAPI APP."""

from fastapi.testclient import TestClient

from app.main import app  # type: ignore

client = TestClient(app)


def test_get_all_recipes():
    """Use this simple test."""
    response = client.get("/cookbook/api/recipes")
    assert response.status_code == 200
