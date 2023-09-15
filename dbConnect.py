
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
cursor=mydb.cursor()
cursor.execute("CREATE DATABASE db_ap")

creaS="CREATE TABLE Studenti( nome varchar(20),cognome varchar(20), eta varchar(100),matricola varchar(100000) PRIMARY KEY,))"
cursor.execute(creaS)


creaE="CREATE TABLE Entrate( orario datetime, matricola varchar(100000),  FOREIGN KEY (matricola) REFERENCES Studenti(matricola))"
cursor.execute(creaE)


creaE="CREATE TABLE Uscite( orario datetime, matricola varchar(100000),  FOREIGN KEY (matricola) REFERENCES Studenti(matricola))"
cursor.execute(creaU)


print(mydb)