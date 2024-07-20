import unittest
from unittest.mock import patch
import sys
import os

# pridat root directory do sys.path, viz strom
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

class TestHome(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('main.Cookie_Manager')
    @patch('main.Tabulka')
    def test_home_template(self, MockTabulka, MockCookieManager):
        # Mock simuluje vracene hodnoty z mych metod v tabulka.py a cookie_manager.py
        mock_tab = MockTabulka.return_value
        mock_tab.random_detail.return_value = [
            {'hlavni_obrazek': 'image1.jpg', 'nazev': 'Record 1', 'autor': 'Autor 1', 'cena': '100', 'link': '#'},
            {'hlavni_obrazek': 'image2.jpg', 'nazev': 'Record 2', 'autor': 'Autor 2', 'cena': '200', 'link': '#'},
            {'hlavni_obrazek': 'image3.jpg', 'nazev': 'Record 3', 'autor': 'Autor 3', 'cena': '300', 'link': '#'}
        ]
        mock_tab.mostly_searched.return_value = {
            'hlavni_obrazek': 'image_most.jpg', 'nazev': 'Most Searched', 'autor': 'Popular Autor', 'cena': '400', 'link': '#'
        }

        mock_cookie = MockCookieManager.return_value
        mock_cookie.get_cookie.return_value = []

        response = self.app.get('/')
        
        # Asserty
        self.assertEqual(response.status_code, 200) #načtení stránky OK
        self.assertIn(b'Record 1', response.data)
        self.assertIn(b'Autor 1', response.data)
        self.assertIn(b'100', response.data)
        self.assertIn(b'Record 2', response.data)
        self.assertIn(b'Autor 2', response.data)
        self.assertIn(b'200', response.data)
        self.assertIn(b'Record 3', response.data)
        self.assertIn(b'Autor 3', response.data)
        self.assertIn(b'300', response.data)
        self.assertIn(b'Most Searched', response.data)
        self.assertIn(b'Popular Autor', response.data)
        self.assertIn(b'400', response.data)

if __name__ == '__main__':  
    #spouští všechny testy, pokud je skript spuštěn přímo.
    unittest.main()
