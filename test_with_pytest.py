import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_always_passes():
    """Test that will always pass successfully."""
    assert True

def test_hello_endpoint(client):
    """Test the hello endpoint returns correct response."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World!' in response.data

def test_status_endpoint(client):
    """Test the status endpoint returns healthy status."""
    response = client.get('/status')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data['result'] == 'OK - healthy'

def test_metrics_endpoint(client):
    """Test the metrics endpoint returns correct metrics."""
    response = client.get('/metrics')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['code'] == 0
    assert 'data' in data
    assert 'UserCount' in data['data']
    assert 'UserCountActive' in data['data']
