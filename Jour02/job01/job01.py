import mysql.connector
 
config = {
  'user': 'root',
  'password': 'FH202417m.',
  'host': 'localhost',
  'database': 'laplateforme'
}
 

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
 

    cursor.execute("SELECT * FROM etudiant")
 
   
    print("Résultat de la requête :")
    for student in cursor:
        print(student)
 
except mysql.connector.Error as err:
    print("Erreur lors de la connexion à la base de données :", err)
 
finally:
   
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()