from fastapi.testclient import TestClient
from app.main import app
from app.routers import challenges as challenges_router

def test_list_challenges_initially_empty():
    challenges_router.challenges.clear()
    client = TestClient(app)
    response = client.get("/challenges/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_challenge_and_list():
    challenges_router.challenges.clear()
    client = TestClient(app)
    challenge_data = {
        "title": "Reto 1",
        "description": "Descripción del reto",
        "difficulty": "básico"
    }
    response = client.post("/challenges/", json=challenge_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()["title"] == challenge_data["title"]

    response = client.get("/challenges/")
    challenges = response.json()
    assert any(ch["title"] == "Reto 1" for ch in challenges)


def test_create_challenge_missing_field():
    challenges_router.challenges.clear()
    client = TestClient(app)
    # Falta 'difficulty'
    challenge_data = {
        "title": "Reto sin dificultad",
        "description": "No tiene dificultad"
    }
    response = client.post("/challenges/", json=challenge_data)
    assert response.status_code == 422
    # Verifica que la respuesta detalle el error en 'difficulty'
    assert any('difficulty' in err['loc'] for err in response.json()['detail'])

def test_create_challenge_wrong_type():
    challenges_router.challenges.clear()
    client = TestClient(app)
    # 'difficulty' debe ser string
    challenge_data = {
        "title": "Reto inválido",
        "description": "Tipo incorrecto",
        "difficulty": 123  # No es string
    }
    response = client.post("/challenges/", json=challenge_data)
    assert response.status_code == 422
    assert any('difficulty' in err['loc'] for err in response.json()['detail'])
