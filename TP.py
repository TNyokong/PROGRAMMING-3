import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "V@1234",
    database = "testdatabes"
)

mycursor = db.cursor()

#mycursor.execure("CREATE DATABASE testdatebes")


#mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint unsigned,personID int Primary key Auto_Increment)")





mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)",("Tim","19"))
db.commit()
mycursor.execute("SELECT * FROM Person")
#mycursor.execute("DESCRIBE Person")

for x in mycursor:
    print (x)
