from app.services.security import hash_password
from app.services.security import verify_password

def test_password_hashing():
    password = "test1234"
    
    hashed_password = hash_password(password)
    
    assert password != hashed_password
    assert verify_password(password, hashed_password)
    assert not verify_password("wrong-password", hashed_password)

def test_register_user(client):
    payload = {
        "email": "test@example.com",
        "password": "test1234"
    }
    response = client.post("/register", json=payload)
    
    assert response.status_code == 201
    
    data = response.json()
    
    assert data["email"] == payload["email"]
    assert "password" not in data
    
def test_register_duplicate_user(client):
    payload = {
        "email": "duplicate@example.com",
        "password": "test1234"
    }
    
    first_response = client.post("/register", json=payload)
    second_response = client.post("/register", json=payload)
    
    assert first_response.status_code == 201
    assert second_response.status_code == 409
 
def test_login(client):
    payload = {
        "email": "login@example.com",
        "password": "test1234"
    }
    
    register_response = client.post("/register", json=payload)
    
    assert register_response.status_code == 201
    
    login_response = client.post("/login", json=payload)
    
    assert login_response.status_code == 200
    assert login_response.json()["message"] == "Login successful"

def test_login_wrong_password(client):
    payload = {
        "email": "wrong-password@example.com",
        "password": "test1234"
    }
    payload_wrong_password = {
        "email": "wrong-password@example.com",
        "password": "wrong-password"
    }
    
    register_response = client.post("/register", json=payload)
    
    assert register_response.status_code == 201
    
    login_response = client.post("/login", json=payload_wrong_password)
    
    assert login_response.status_code == 401
    assert login_response.json()["detail"] == "Invalid credentials"
    
def test_login_nonexistent_user(client):
    payload = {
        "email": "non-existent-user@example.com",
        "password": "test1234"
    }
    
    login_response = client.post("/login", json=payload)
    
    assert login_response.status_code == 401
    assert login_response.json()["detail"] == "Invalid credentials"