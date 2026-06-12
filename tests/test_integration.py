import pytest
from src.database import DatabaseConnection
from src.calculator import Calculator


class TestIntegration:
    def setup_method(self):
        self.db = DatabaseConnection()
        self.calc = Calculator()

    def test_database_connection(self):
        result = self.db.connect()
        assert result == "Connected to database"
        assert self.db.connected is True

    def test_database_query(self):
        self.db.connect()
        results = self.db.query("SELECT * FROM users")
        assert len(results) == 1
        assert results[0]["name"] == "test"

    def test_calculator_with_db_flow(self):
        self.db.connect()
        db_data = self.db.query("SELECT value FROM config")[0]
        result = self.calc.add(10, db_data["id"])
        assert result == 11

    def test_database_not_connected(self):
        with pytest.raises(ConnectionError):
            self.db.query("SELECT * FROM users")

    def teardown_method(self):
        self.db.disconnect()
