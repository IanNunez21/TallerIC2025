import pytest
from src.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_get_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Calculadora" in resp.data

def test_post_suma(client):
    resp = client.post("/", data={"a": "2", "op": "+", "b": "3"})
    assert b"Resultado: 5.0" in resp.data

def test_post_division_zero(client):
    resp = client.post("/", data={"a": "1", "op": "/", "b": "0"})
    assert b"Error: Division por cero no es permitida" in resp.data
