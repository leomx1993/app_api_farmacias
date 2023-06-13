import pytest
import requests

@pytest.fixture
def base_url():
    return "http://localhost:8000"  

# Testes endpoint de autenticação e endpoints da API:

def test_auth(base_url):
    url = f"{base_url}/auth"
    response = requests.post(url)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_patients(base_url):
    url = f"{base_url}/patients"
    response = requests.get(url)
    assert response.status_code == 401

    # token

    auth_url = f"{base_url}/auth"
    auth_response = requests.post(auth_url)
    assert auth_response.status_code == 200
    access_token = auth_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert "patients" in response.json()

def test_get_pharmacies(base_url):
    url = f"{base_url}/pharmacies"
    response = requests.get(url)
    assert response.status_code == 401

    # token

    auth_url = f"{base_url}/auth"
    auth_response = requests.post(auth_url)
    assert auth_response.status_code == 200
    access_token = auth_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert "pharmacies" in response.json()


def test_get_transactions(base_url):
    url = f"{base_url}/transactions"
    response = requests.get(url)
    assert response.status_code == 401

    

    auth_url = f"{base_url}/auth"
    auth_response = requests.post(auth_url)
    assert auth_response.status_code == 200
    access_token = auth_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert "transactions" in response.json()
