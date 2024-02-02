import mysql.connector
 
class DefZoo:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="FH202417m.",
            database="zoo"
        )
        self.cursor = self.conn.cursor()
 
    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()
 
    def supprimer_animal(self, id_animal):
        query = "DELETE FROM animal WHERE id = %s"
        values = (id_animal,)
        self.cursor.execute(query, values)
        self.conn.commit()
 
    def modifier_animal(self, id_animal, nom, race, id_cage, date_naissance, pays_origine):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, id_animal)
        self.cursor.execute(query, values)
        self.conn.commit()
 
    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        return self.cursor.fetchall()
 
    
 
    def __del__(self):
        self.cursor.close()
        self.conn.close()
 