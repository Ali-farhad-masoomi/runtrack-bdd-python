import mysql.connector
 
 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FH202417m.",
    database="laplateforme"
)
 
cursor = conn.cursor()
cursor.execute("SELECT superficie FROM etage ;")
superficies = cursor.fetchall()
superficieTotal = 0
for superficie in superficies:
 
    superficieTotal = superficieTotal + superficie[0]
print('La superficie de LaPlateforme est de', superficieTotal, 'm2')
 
cursor.close()
conn.close()