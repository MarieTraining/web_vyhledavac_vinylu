import mysql.connector as db
import numpy as np

class Tabulka:
    def __init__(self):
        self.mydb = db.connect(
            host="localhost",
            user="root",
            password="***",
            database="dB_vyhledavac_desek",
            port=3306 
        )
        self.cursor = self.mydb.cursor(dictionary=True)
        
        """
#nove pro pythonanywhere
class Tabulka:
    def __init__(self):
        self.mydb = db.connect(
            host="MarieTraining.mysql.pythonanywhere-services.com",
            user="MarieTraining",  # PythonAnywhere username
            password="***",  # Database password
            database="MarieTraining$dB_vyhledavac_desek",
            port=3306
        )
        self.cursor = self.mydb.cursor(dictionary=True)
#nove pro pythonanywhere
        """
    def print_table(self):
        self.cursor.execute(f"select hlavni_obrazek, nazev, autor, rok, vydavatelstvi, cena, link from gramodeska ")
        dataset = self.cursor.fetchall()
        return (dataset)
    
    def search_table(self, hledany_vyraz):
        self.cursor.execute(f"select hlavni_obrazek, nazev, autor, rok, vydavatelstvi, cena, link, IDdeska from gramodeska WHERE nazev LIKE '%{hledany_vyraz}%'or autor LIKE '%{hledany_vyraz}%'")
        tabulka_search = self.cursor.fetchall()
        return (tabulka_search)
      
    def random_detail(self):
        self.cursor.execute(f"select hlavni_obrazek, nazev, autor,rok, cena, link FROM gramodeska ORDER BY timestamp DESC LIMIT 20 ")
        dataset = self.cursor.fetchall()
        random_detail = np.random.choice(dataset, 3, replace=False)
        return (random_detail)  
    
    def detail (self, ID):
        self.cursor.execute(f"select hlavni_obrazek, nazev, autor, rok, link FROM gramodeska where IDdeska = {ID} ")
        detail = self.cursor.fetchone()
        return(detail)
    
    def mostly_searched(self, list_cookies):
        list_cookies = [item for item in list_cookies if item]
        if not list_cookies:
            return None
        nejhledanejsi_vyraz = sorted(list_cookies, key=lambda x: list_cookies.count(x), reverse=True)[0]
        self.cursor.execute(f"select hlavni_obrazek, nazev, autor,rok, cena, link FROM gramodeska WHERE nazev LIKE '%{nejhledanejsi_vyraz}%'or autor LIKE '%{nejhledanejsi_vyraz}%'")
        nejcasteji_hledany_detail = self.cursor.fetchone()
        print("nejcateji hledany: ", nejhledanejsi_vyraz)
        print(list_cookies)
        return nejcasteji_hledany_detail

    def exit (self):
        self.cursor.close()
        self.mydb.close()


"""
hledany_vyraz = "2"
tabulka= Tabulka().print_table()
tabulka3 =Tabulka().search_table(hledany_vyraz)
tabulka4 =Tabulka().random_detail()
x= Tabulka().detail(2)
list_of_cookies = ['hledane vyrazy:', 'naz', None, 'naz', '1','2', None, '5', '2', None, None, 'naz', '1',None, 'naz', None, 'naz', '2', '2', '2', '2', '2', '2', '1', '2', 'naz', 'naz4', 'fff', '1', '2', 'g', 'naz', '1', 'h', '1', '4', '', 'fff', '4', '', '2', 'naz', '', 'naz', 'nhaz', 'nz', '', '190', 'naz', '', '', '', '', 'naz', '', 'naz', '', 'naz', 'naz', 'naz', '2']
tabulka5 = Tabulka().mostly_searched(list_of_cookies)
list_of_cookies = ['hledane vyrazy:', 'naz', None, 'naz', '1','2', None, '5', '2', None, None, 'naz', '1',None, 'naz', None, 'naz', '2', '2', '2', '2', '2', '2', '1', '2', 'naz', 'naz4', 'fff', '1', '2', 'g', 'naz', '1', 'h', '1', '4', '', 'fff', '4', '', '2', 'naz', '', 'naz', 'nhaz', 'nz', '', '190', 'naz', '', '', '', '', 'naz', '', 'naz', '', 'naz', 'naz', 'naz', '2']
tabulka5 = Tabulka().mostly_searched(list_of_cookies)
"""
