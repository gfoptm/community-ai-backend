from fastapi.testclient import TestClient
from app.main import app

def test_liveness():
    r=TestClient(app).get('/health/live')
    assert r.status_code == 200 and r.json()['status']=='ok'

def test_mock_chat():
    r=TestClient(app).post('/api/v1/chat', json={'message':'hello'})
    assert r.status_code == 200 and 'Mock response' in r.json()['answer']
