import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
  
)
# print(mydb)
mycursor = mydb.cursor()

# #query = "CREATE DATABASE pythonmysql"
# query = "show databases"

# mycursor.execute(query)

# for x in mycursor:
#   print(x)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="pythonmysql"
  
)
# query= "CREATE TABLE utenti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50), indirizzo VARCHAR(50))"
query = "INSERT INTO utenti (nome, indirizzo) VALUES (%s, %s)"
#valori = ("John Doe", "Via Roma 12")
valori = [("Alice", "Via Milano 34"), 
          ("Bob", "Via Firenze 56" ), 
          ("Charlie", "Via Torino 78" )]
mycursor = mydb.cursor()
mycursor.executemany(query,valori)

mydb.commit() #mydb.commit() committa le modifiche al database
print(mycursor.rowcount, "record inserted.") #mycursor.rowcount è il numero di righe inserite
#mycursor.lastrowid da utilizzare per l'id dell'ultimo record inserito
