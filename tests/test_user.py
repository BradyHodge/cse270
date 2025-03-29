import pytest
import requests

@pytest.fixture
def mock_server(requests_mock):
    """
    Set up mock responses for the server.
    """
    # Mock the unauthorized response
    requests_mock.get(
        "http://127.0.0.1:8000/users?username=admin&password=admin", 
        text="", 
        status_code=401
    )
    
    # Mock the authorized response
    requests_mock.get(
        "http://127.0.0.1:8000/users?username=admin&password=qwerty", 
        text="", 
        status_code=200
    )
    
    return requests_mock

def test_unauthorized_access(mock_server):
    """
    Test that accessing /users endpoint with invalid credentials returns 401 Unauthorized.
    """
    # Define the endpoint and parameters
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }
    
    # Send the request
    response = requests.get(url, params=params)
    
    # Assert the response status code is 401
    assert response.status_code == 401
    
    # Assert the response body is empty
    assert response.text == ""

def test_authorized_access(mock_server):
    """
    Test that accessing /users endpoint with valid credentials returns 200 OK.
    """
    # Define the endpoint and parameters
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }
    
    # Send the request
    response = requests.get(url, params=params)
    
    # Assert the response status code is 200
    assert response.status_code == 200
    
    # Assert the response body is empty
    assert response.text == ""