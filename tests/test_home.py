#### INTERGRATION test ####
# Tento má simulovat HTTP požadavky na různé URL a kontroluje, zda vrácené odpovědi obsahují očekávané údaje. 
# Testuje, jak aplikace jako celek reaguje na různé vstupy a zda správně integruje komponenty jako Tabulka a Cookie_Manager.
"""Test simuluje výstupní data z Cookie_Manager a Tabulka a ověřuje, zda jsou tato data správně 
integrována a zobrazená na hlavní stránce aplikace"""
# Potřebuje zaplý Xammp/databázi

import unittest
from unittest.mock import patch
import sys
import os

# pridat root directory do sys.path, viz strom
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

class TestHome(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client() #testovací klient pro Flask app. Umožňuje simulovat HTTP požadavky na app bez serveru.
        self.app.testing = True #režim testování (lepší hlášky)

    @patch('main.Cookie_Manager')#simulace Cookie_Manager v modulu main.py; bez toho nefunguje Mock
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
        self.assertEqual(response.status_code, 200) #chyba 200 =načtení stránky OK; assert ==
        self.assertIn(b'Record 1', response.data) #in jako instance - zda je stejny objekt
            # kontrola zda specifické textové řetězce (v podobě bajtů) jsou obsaženy v datech odpovědi (očekávaný obsah je přítomen na stránce, která byla vrácena aplikací)
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
    unittest.main()