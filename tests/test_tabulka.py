#### UNIT test ####
# účel: otestovat metody z tabulka.py

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# pridat root directory do sys.path, viz strom, aby test nasel tabulka.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tabulka import Tabulka

class TestTabulka(unittest.TestCase):
    #nahrazuje metodu db.connect v modulu tabulka mockovaným objektem
    @patch('tabulka.db.connect') 
    
    # metoda set up se spouští před každým testem a nastaví novou instanci třídy Tabulka a "našvindlované(Magic Mock)"  připojení k databázi 
    def setUp(self, mock_db_connect):
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        mock_db_connect.return_value = self.mock_connection
        self.mock_connection.cursor.return_value = self.mock_cursor
        self.tabulka = Tabulka()
    
    #Test1: ověřuje, že print_table vrátí správné výsledky + že nemám chybu v SQL dotazu volám ji jednou
    def test_print_table(self):
        self.mock_cursor.fetchall.return_value = [{'nazev': 'Test Print'}] #místo skutečné hodnoty z DB cursor vrátí seznam se slovníkem obsahujícím [{'nazev': 'Test Print'}]
        result = self.tabulka.print_table()
        self.mock_cursor.execute.assert_called_once_with("select hlavni_obrazek, nazev, autor, rok, vydavatelstvi, cena, link from gramodeska ")
        self.assertEqual(result, [{'nazev': 'Test Print'}])

    #Test2: ověřuje, že search_table vrátí správné výsledky + že nemám chybu v SQL dotazu volám ji jednou
    def test_search_table(self):
        self.mock_cursor.fetchall.return_value = [{'nazev': 'Test Search', 'autor': 'Author'}]
        result = self.tabulka.search_table('test')
        self.mock_cursor.execute.assert_called_once_with("select hlavni_obrazek, nazev, autor, rok, vydavatelstvi, cena, link, IDdeska from gramodeska WHERE nazev LIKE '%test%'or autor LIKE '%test%'")
        self.assertEqual(result, [{'nazev': 'Test Search', 'autor': 'Author'}])

    #Test3:
    def test_random_detail(self):
        self.mock_cursor.fetchall.return_value = [
            {'nazev': 'Test1', 'autor': 'Autor1'},
            {'nazev': 'Test2', 'autor': 'Autor2'},
            {'nazev': 'Test3', 'autor': 'Autor3'}
        ]
        with patch('numpy.random.choice', return_value=[
            {'nazev': 'Test1', 'autor': 'Autor1'},
            {'nazev': 'Test2', 'autor': 'Autor2'},
            {'nazev': 'Test3', 'autor': 'Autor3'}
        ]):
            result = self.tabulka.random_detail()
            self.mock_cursor.execute.assert_called_once_with("select hlavni_obrazek, nazev, autor,rok, cena, link FROM gramodeska ORDER BY timestamp DESC LIMIT 20 ")
            self.assertEqual(len(result), 3)
            self.assertIn({'nazev': 'Test1', 'autor': 'Autor1'}, result)

    #Test4: ověřuje, že "detail" vrátí správné výsledky + že nemám chybu v SQL dotazu volám ji jednou
    def test_detail(self):
        self.mock_cursor.fetchone.return_value = {'nazev': 'Test Detail', 'autor': 'Autor Detail'}
        result = self.tabulka.detail(1)
        self.mock_cursor.execute.assert_called_once_with("select hlavni_obrazek, nazev, autor, rok, link FROM gramodeska where IDdeska = 1 ")
        self.assertEqual(result, {'nazev': 'Test Detail', 'autor': 'Autor Detail'})

    #Test5: ověřuje, že "mostly_searched" vrátí správné výsledky + že nemám chybu v SQL dotazu volám ji jednou
    def test_mostly_searched(self):
        self.mock_cursor.fetchone.return_value = {'nazev': 'Test Mostly Searched'}
        list_of_cookies = ['test1', 'test2', 'test1', 'test3', 'test1']
        result = self.tabulka.mostly_searched(list_of_cookies)
        self.mock_cursor.execute.assert_called_once_with("select hlavni_obrazek, nazev, autor,rok, cena, link FROM gramodeska WHERE nazev LIKE '%test1%'or autor LIKE '%test1%'")
        self.assertEqual(result, {'nazev': 'Test Mostly Searched'})
    
    #Test6
    def test_exit(self):
        # nasimuluju odchod
        self.tabulka.exit()
        # overim ze oboji bylo volano
        self.mock_cursor.close.assert_called_once()
        self.mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()