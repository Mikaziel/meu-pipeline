import pytest
from src.calculator import Calculator
from src.database import DatabaseConnection


@pytest.fixture
def calculator():
    return Calculator()


@pytest.fixture
def database():
    db = DatabaseConnection()
    yield db
    if db.connected:
        db.disconnect()
