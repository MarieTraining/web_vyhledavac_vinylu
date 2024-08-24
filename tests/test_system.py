#pokus o systémový test, není hotov, ale chci to mít uložené
import unittest
import requests
import mysql.connector
import os

class TestSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Nastavení, které se provádí jednou před spuštěním všech testů"""
        # Set the Flask app environment variable
        os.environ['FLASK_APP'] = r'C:\Users\kofolník\Desktop\Python\projekt_Web_Vyhledavac_Vinylu\main.py'

        # Byly problémy s připojením k Flasku: Start the Flask application if it's not running
        import subprocess
        cls.flask_process = subprocess.Popen(['flask', 'run', '--host=127.0.0.1', '--port=5000'])

        # Připojení k databázi a vytvoření testových dat
        cls.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            #password="your_password",  
            database="test_database",
            port=3306 
        )
        cls.cursor = cls.db_connection.cursor()
        # Vytvoření tabulky, pokud ještě neexistuje
        cls.cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255)
            )
        """)
        # Vymazání všech existujících záznamů
        cls.cursor.execute("DELETE FROM test_table")
        # Vložení testovacího záznamu
        cls.cursor.execute("INSERT INTO test_table (name) VALUES ('Test Record')")
        cls.db_connection.commit()

    @classmethod
    def tearDownClass(cls):
        """Úklid po všech testech"""
        cls.cursor.execute("DROP TABLE IF EXISTS test_table")
        cls.db_connection.close()

    def setUp(self):
        """Nastavení před každým testem"""
        self.base_url = 'http://127.0.0.1:5000'

    def test_database_interaction(self):
        """Test, zda aplikace správně interaguje s databází"""
        response = requests.get(f"{self.base_url}/vyhledani?hledany_vyraz=Test Record")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Record', response.content)

    def test_full_application_flow(self):
        """Test kompletního toku aplikace"""
        # Odpověď home page
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)
        #obsah stránky home
        #self.assertIn(b'Domovská stránka', response.content)  # Page title
        self.assertIn(b'NOVINKY:', response.content)          # Example section text

        # Testing the search functionality
        response = requests.get(f"{self.base_url}/vyhledani?hledany_vyraz=Test Record")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Record', response.content)


if __name__ == '__main__':
    unittest.main()
