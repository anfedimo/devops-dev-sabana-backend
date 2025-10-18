import pytest
from fastapi.testclient import TestClient
from app.main import app, Challenge, challenges

@pytest.fixture(autouse=True)
def clear_challenges():
    challenges.clear()

# Fixture para el cliente de prueba
@pytest.fixture
def client():
    return TestClient(app)

# Test para la ruta raíz
def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Somos el grupo 14 de Arquitectura de Software" in response.text

# Test para el health check
def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# Test para listar challenges (vacío inicialmente)
def test_list_challenges_empty(client):
    response = client.get("/challenges")
    assert response.status_code == 200
    assert response.json() == []

# Test para crear un nuevo challenge
def test_create_challenge(client):
    test_challenge = {
        "title": "Ahorrar 10%",
        "description": "Ahorrar el 10% del salario mensual",
        "difficulty": "intermedio"
    }

    response = client.post("/challenges", json=test_challenge)
    assert response.status_code == 201
    assert response.json()["title"] == test_challenge["title"]

    # Verificar que se agregó a la lista
    response = client.get("/challenges")
    assert len(response.json()) == 1

# Test para validación de difficulty
def test_invalid_difficulty(client):
    test_challenge = {
        "title": "Reto inválido",
        "description": "Descripción",
        "difficulty": "invalido"  # Valor no permitido
    }

    response = client.post("/challenges", json=test_challenge)
    assert response.status_code == 422  # Unprocessable Entity
    assert "difficulty" in response.text

