# test_app.py
import unittest
from app import app

class FlaskTest(unittest.TestCase):
    def test_home(self):
        tester = app.test_client()  # ❌ remove 'self' here
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

