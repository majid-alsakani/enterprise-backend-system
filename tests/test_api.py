from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_status():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()['status'] == 'running'


def test_demo_login():
    response = client.post('/api/login')
    assert response.status_code == 200
    assert response.json()['token'] == 'example_jwt_token_for_demonstration'


def test_login_requires_post():
    assert client.get('/api/login').status_code == 405


def test_unknown_route():
    assert client.get('/missing').status_code == 404


def test_openapi_contract():
    schema = client.get('/openapi.json').json()
    assert schema['info']['version'] == '1.0.0'
    assert set(schema['paths']) == {'/', '/api/login'}
    assert 'post' in schema['paths']['/api/login']
