import pytest
from pydantic import ValidationError
from app.models import Challenge

def test_challenge_creation_valid():
    data = {
        "title": "Ahorra el 10% mensual",
        "description": "Reto de ahorro mensual",
        "difficulty": "intermedio"
    }
    challenge = Challenge(**data)
    assert challenge.title == "Ahorra el 10% mensual"
    assert challenge.description == "Reto de ahorro mensual"
    assert challenge.difficulty == "intermedio"

def test_challenge_missing_fields():
    # Falta 'difficulty'
    data = {
        "title": "Reto sin dificultad",
        "description": "Falta campo"
    }
    with pytest.raises(ValidationError):
        Challenge(**data)

def test_challenge_wrong_type():
    # 'difficulty' como int, debería ser str
    data = {
        "title": "Reto tipo incorrecto",
        "description": "Tipo de dificultad incorrecto",
        "difficulty": 123
    }
    with pytest.raises(ValidationError):
        Challenge(**data)

def test_challenge_creation_valid():
    """
    Escenario: Instanciación correcta del modelo Challenge.
    Dado (Arrange): Un diccionario con datos válidos (título, descripción, dificultad).
    Cuando (Act): Se instancia el modelo Pydantic 'Challenge'.
    Entonces (Assert): Las propiedades del objeto coinciden con los datos ingresados.
    """
    # Arrange
    data = {
        "title": "Ahorra el 10% mensual",
        "description": "Reto de ahorro mensual",
        "difficulty": "intermedio"
    }

    # Act
    challenge = Challenge(**data)

    # Assert
    assert challenge.title == "Ahorra el 10% mensual", "El título no coincide"
    assert challenge.description == "Reto de ahorro mensual", "La descripción no coincide"
    assert challenge.difficulty == "intermedio", "La dificultad no coincide"