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

def test_create_challenge_successfully(client):
    """
    Escenario: Creación exitosa de un nuevo reto financiero.
    Dado (Given/Arrange): Un payload válido con título, descripción y dificultad permitida.
    Cuando (When/Act): Se envía una petición POST al endpoint '/challenges'.
    Entonces (Then/Assert): El sistema retorna un código 201 y el reto se almacena correctamente.
    """
    # 1. Arrange (Dado / Given)
    valid_payload = {
        "title": "Fondo de Emergencia",
        "description": "Ahorrar 3 meses de gastos fijos",
        "difficulty": "avanzado"
    }

    # 2. Act (Cuando / When)
    response = client.post("/challenges", json=valid_payload)

    # 3. Assert (Entonces / Then)
    assert response.status_code == 201, "El código de estado debe ser 201 Created"

    response_data = response.json()
    assert response_data["title"] == valid_payload["title"], "El título debe coincidir con el payload"

    # Verificación de estado en el sistema (evitar falsos positivos)
    verify_response = client.get("/challenges")
    assert any(ch["title"] == valid_payload["title"] for ch in verify_response.json()), "El reto debe persistir en el sistema"
