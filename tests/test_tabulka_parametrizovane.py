#### UNIT test ####
# pokus o parametrizaci testů z test_tabulka.py
# účel: v rámci studia zamezit opakování stejných kódů, zlepšit údržbu/přidávání testů a srozumitelnost
# kód není kratší, což původně měl být účel:-))

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Přidat root directory do sys.path, aby test našel tabulka.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tabulka import Tabulka

class TestTabulka(unittest.TestCase):
    @patch('tabulka.db.connect')
    def setUp(self, mock_db_connect):
        # Vytvoření mock objektů pro připojení k databázi a kurzor
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        mock_db_connect.return_value = self.mock_connection
        self.mock_connection.cursor.return_value = self.mock_cursor
        self.tabulka = Tabulka()

    def test_queries(self):
        # Definice testovacích případů
        test_cases = [
            {
                'method': 'print_table',
                'query': "select hlavni_obrazek, nazev, autor, rok, vydavatelstvi, cena, link from gramodeska ",
                'expected_result': [{'nazev': 'Test Print'}],
                'mock_return': [{'nazev': 'Test Print'}],
                'fetch_method': 'fetchall'  
            },
            {
                'method': 'search_table',
                'query': "select hlavni_obrazek, nazev, autor, rok, vydavatelstvi, cena, link, IDdeska from gramodeska WHERE nazev LIKE '%test%'or autor LIKE '%test%'",
                'expected_result': [{'nazev': 'Test Search', 'autor': 'Author'}],
                'mock_return': [{'nazev': 'Test Search', 'autor': 'Author'}],
                'args': ('test',),
                'fetch_method': 'fetchall'  
            },
            {
                'method': 'random_detail',
                'query': "select hlavni_obrazek, nazev, autor,rok, cena, link FROM gramodeska ORDER BY timestamp DESC LIMIT 20 ",
                'expected_result': [{'nazev': 'Test1', 'autor': 'Autor1'}, {'nazev': 'Test2', 'autor': 'Autor2'}, {'nazev': 'Test3', 'autor': 'Autor3'}],
                'mock_return': [{'nazev': 'Test1', 'autor': 'Autor1'}, {'nazev': 'Test2', 'autor': 'Autor2'}, {'nazev': 'Test3', 'autor': 'Autor3'}],
                'fetch_method': 'fetchall',  
                'patch': 'numpy.random.choice'  # Patche pro numpy.random.choice
            },
            {
                'method': 'detail',
                'query': "select hlavni_obrazek, nazev, autor, rok, link FROM gramodeska where IDdeska = 1 ",
                'expected_result': {'nazev': 'Test Detail', 'autor': 'Autor Detail'},
                'mock_return': {'nazev': 'Test Detail', 'autor': 'Autor Detail'},
                'args': (1,),
                'fetch_method': 'fetchone' 
            },
            {
                'method': 'mostly_searched',
                'query': "select hlavni_obrazek, nazev, autor,rok, cena, link FROM gramodeska WHERE nazev LIKE '%test1%'or autor LIKE '%test1%'",
                'expected_result': {'nazev': 'Test Mostly Searched'},
                'mock_return': {'nazev': 'Test Mostly Searched'},
                'args': (['test1', 'test2', 'test1', 'test3', 'test1'],),
                'fetch_method': 'fetchone' 
            }
        ]

        for case in test_cases:
            with self.subTest(case=case):
                # Nastavit návratovou hodnotu mock objektu na základě fetch metody (nechtěla jsem měnit původní kód tabulka.py)
                if case['fetch_method'] == 'fetchall':
                    self.mock_cursor.fetchall.return_value = case['mock_return']
                elif case['fetch_method'] == 'fetchone':
                    self.mock_cursor.fetchone.return_value = case['mock_return']
                
                # Použít patch, pokud je potřeba
                if 'patch' in case:
                    with patch(case['patch'], return_value=case['mock_return']):
                        result = getattr(self.tabulka, case['method'])(*case.get('args', ()))
                else:
                    result = getattr(self.tabulka, case['method'])(*case.get('args', ()))
                
                # Zkontrolovat, zda byl SQL dotaz proveden správně
                self.mock_cursor.execute.assert_called_with(case['query'])
                
                # Zkontrolovat, zda výsledek odpovídá očekávané hodnotě
                self.assertEqual(result, case['expected_result'])

    def test_exit(self):
        # Nasimuluji odchod
        self.tabulka.exit()
        # Overím, že obě volání byla provedena
        self.mock_cursor.close.assert_called_once()
        self.mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
