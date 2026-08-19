import pytest
import os
from app import app, init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    init_db()
    with app.test_client() as client:
        yield client
    if os.path.exists('users.db'):
        os.remove('users.db')

def test_get_user_valid(client):
    response = client.get('/user?username=admin')
    assert b'superuser' in response.data
    assert response.status_code == 200

def test_get_user_invalid(client):
    response = client.get('/user?username=hacker')
    assert b'[]' in response.data
