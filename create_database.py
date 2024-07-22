import mysql.connector as db
import csv
import os
try:
    mydb = db.connect(
        host="localhost",
        user="root",
        port=3306
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db_gramodesky")
    mycursor.execute("USE db_gramodesky")

    # Tabulka gramodeska
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS gramodeska (
            IDdeska int(200) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nazev varchar(200) NOT NULL,
            autor varchar(200) NOT NULL,
            rok int(200) DEFAULT NULL,
            vydavatelstvi varchar(200) NOT NULL,
            cena int(200) NOT NULL,
            stav int(200) DEFAULT NULL,
            hlavni_obrazek varchar(200) NOT NULL,
            link varchar(200) DEFAULT NULL,
            obchod int(200) NOT NULL,
            timestamp timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;
    """)
    mydb.commit()
    #Data do tab gramodeska
    insert_query_gramodeska = """
        INSERT INTO gramodeska (nazev, autor, rok, vydavatelstvi, cena, stav, hlavni_obrazek, link, obchod, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    #file_path = r"C:\Users\kofolník\Desktop\Python\projekt_Web_Vyhledavac_Vinylu\datas\gramodesky.csv"
    directory = os.path.dirname(__file__) 
    file_path = os.path.join(directory,"datas","gramodesky.csv")
    print(file_path)

    with open(file_path, "r", encoding="utf-8") as soubor:
        reader = csv.reader(soubor)
        mylist = []
        next(reader, None) # Skip the header row
        for radek in reader:
            if radek: mylist.append(tuple(radek))  # Convert each row to a tuple
        #print(mylist)
    records_gramodeska = mylist
    mycursor.executemany(insert_query_gramodeska, records_gramodeska)
    mydb.commit()
    ###########################
    """data mají být ve tvaru gramodeska_short.csv:    
        records_gramodeska = [
            ('nazev2', 'autor2', 1902, 'vydavatelstvi2', 222, None, 'https://upload.wikimedia.org/wikipedia/commons/c/cd/Number_2_in_light_blue_rounded_square.svg', 'https://cs.wikipedia.org/', 2, '2024-06-19 12:57:32'),
            ('přednazevpo', 'autor4', 1904, 'vydavatelstvi4', 444, None, 'https://upload.wikimedia.org/wikipedia/commons/4/45/Eo_circle_blue_number-4.svg', 'https://cs.wikipedia.org/', 1, '2024-06-19 12:58:01'),
            ('nazev1', 'autor1', 1901, 'vydavatelstvi1', 111, None, 'https://upload.wikimedia.org/wikipedia/commons/f/fd/Eo_circle_blue_number-1.svg', 'https://cs.wikipedia.org/', 1, '2024-06-19 12:58:09'),
            ('nazev3', 'autor3', 1903, 'vadavatelstvi3', 333, None, 'https://upload.wikimedia.org/wikipedia/commons/3/3e/Eo_circle_blue_number-3.svg', 'https://cs.wikipedia.org/', 1, '2024-06-19 12:58:19'),
            ('názevžšč_', 'autor5', None, 'vydavatelstvi5', 555, None, 'https://upload.wikimedia.org/wikipedia/commons/d/db/Eo_circle_deep-orange_white_number-5.svg', 'https://cs.wikipedia.org/', 2, '2024-06-19 12:58:35'),
            ('muj nazev6', 'muj autor 6', 1906, 'mujm vydavatelstvi 6', 666, None, 'https://media.hornbach.cz/hb/packshot/as.47360528.jpg?dvid=7', 'https://cs.wikipedia.org/', 1, '2024-06-19 12:58:52')
        ]"""
    ###########################

    # Tabulka obchod
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS obchod (
            IDobchod int(200) NOT NULL PRIMARY KEY,
            jmeno varchar(200) NOT NULL,
            mesto varchar(200) NOT NULL,
            link varchar(200) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;
    """)

    # Data do tabulka obchod
    insert_query_obchod = """
        INSERT INTO obchod (IDobchod, jmeno, mesto, link)
        VALUES (%s, %s, %s, %s)
    """
    records_obchod = [
        (1, 'Čejka', 'Praha', 'http://www.antikvariat-cejka.com/info/contact'),
        (2, 'Avion', 'Liberec', 'https://www.antikavion.cz/kontakt')
    ]

    mycursor.executemany(insert_query_obchod, records_obchod)
    mydb.commit()

    # Přidej cizí klíč
    mycursor.execute("""
        ALTER TABLE `gramodeska`
        ADD CONSTRAINT `gramodeska_ibfk_1` FOREIGN KEY (`obchod`) REFERENCES `obchod` (`IDobchod`)
    """)
    mydb.commit()
    print("Database creation, table creation, and data insertion successful!")

except db.Error as e:
    print(f"Error creating database/table or inserting data: {e}")

finally: 
    if mydb:
        mydb.close()