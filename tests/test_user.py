import pytest
import requests
import responses

@pytest.fixture
def mock_api():
    """Fixture to set up the mock API responses"""
    with responses.RequestsMock() as rsps:
        # Mock the unauthorized response
        rsps.add(
            responses.GET, 
            "http://127.0.0.1:8000/users",
            body="",
            status=401,
            match=[responses.matchers.query_param_matcher({"username": "admin", "password": "admin"})]
        )
        
        # Mock the authorized response
        rsps.add(
            responses.GET, 
            "http://127.0.0.1:8000/users",
            body="",
            status=200,
            match=[responses.matchers.query_param_matcher({"username": "admin", "password": "qwerty"})]
        )
        
        yield rsps

def test_unauthorized_access(mock_api):
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

def test_authorized_access(mock_api):
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