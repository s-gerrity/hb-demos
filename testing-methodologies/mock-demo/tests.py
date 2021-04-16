from unittest import TestCase
from model import Employee, Department, connect_to_db, db, example_data
from server import app
import server


class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_find_employee(self):
        """Can we find an employee in the sample data?"""

        leonard = Employee.query.filter(Employee.name == "Leonard").first()
        self.assertEqual(leonard.name, "Leonard")

    def test_emps_by_state(self):
        """Find employees in a state."""

        result = self.client.get("/emps-by-state?state=California")

        self.assertIn(b"Nadine", result.data)


class MockFlaskTests(TestCase):
    """Flask tests that show off mocking."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

        # Make mock
        def _mock_state_to_code(state_name):
            return "CA"

        server.state_to_code = _mock_state_to_code

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_emps_by_state_with_mock(self):
        """Find employees in a state."""

        result = self.client.get('/emps-by-state?state=California')
        self.assertIn(b"Nadine", result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()
