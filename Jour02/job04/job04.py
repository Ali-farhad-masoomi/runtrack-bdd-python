import mysql.connector
 
host = "localhost"
user = "root"
password = "FH202417m."
database = "laplateforme"
 
 
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
 
 
cursor = conn.cursor()
 
cursor.execute("SELECT * FROM salle;")
 
 
results = cursor.fetchall()
 
 
for row in results:
    print(row)
 
 
cursor.close()
conn.close()