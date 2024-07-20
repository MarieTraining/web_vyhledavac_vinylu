import unittest
from unittest.mock import patch
import sys
import os

# pridat root directory do sys.path, viz strom, aby test nasel main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('main.Cookie_Manager')
    @patch('main.Tabulka')
    def test_home(self, MockTabulka, MockCookieManager):
        mock_tab = MockTabulka.return_value
        mock_tab.random_detail.return_value = [{'nazev': 'Test1'}, {'nazev': 'Test2'}, {'nazev': 'Test3'}]
        mock_tab.mostly_searched.return_value = {'nazev': 'Test'}

        mock_cookie = MockCookieManager.return_value
        mock_cookie.get_cookie.return_value = []

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test1', response.data)
        self.assertIn(b'Test2', response.data)
        self.assertIn(b'Test3', response.data)
        self.assertIn(b'Test', response.data)

    @patch('main.Cookie_Manager')
    @patch('main.Tabulka')
    def test_vyhledani(self, MockTabulka, MockCookieManager):
        mock_tab = MockTabulka.return_value
        mock_tab.print_table.return_value = []
        mock_tab.search_table.return_value = [{'nazev': 'Test Search', 'autor': 'Autor', 'rok': 2020, 'vydavatelstvi': 'Publisher', 'cena': 100, 'IDdeska': 1}]

        mock_cookie = MockCookieManager.return_value
        mock_cookie.get_cookie.return_value = []

        response = self.app.get('/vyhledani?hledany_vyraz=test')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Search', response.data)
        self.assertIn(b'Autor', response.data)
        self.assertIn(b'2020', response.data)
        self.assertIn(b'Publisher', response.data)
        self.assertIn(b'100', response.data)

    @patch('main.Tabulka')
    def test_detail(self, MockTabulka):
        mock_tab = MockTabulka.return_value
        mock_tab.detail.return_value = {'nazev': 'Test Detail', 'autor': 'Autor Detail', 'rok': 2021}

        response = self.app.get('/detail?IDdeska=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Detail', response.data)
        self.assertIn(b'Autor Detail', response.data)
        self.assertIn(b'2021', response.data)

if __name__ == '__main__':
    unittest.main()