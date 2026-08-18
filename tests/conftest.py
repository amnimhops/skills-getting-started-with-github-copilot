import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Fixture providing a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def sample_email():
    """Fixture providing a sample email for testing"""
    return "test.student@mergington.edu"


@pytest.fixture
def sample_activity():
    """Fixture providing a sample activity name for testing"""
    return "Chess Club"
