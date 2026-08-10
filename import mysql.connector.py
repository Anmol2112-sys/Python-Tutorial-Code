import mysql.connector
mysql.connector.connect(host="localhost",user="anmol",password="Anmol@21")
mycursor=mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
	print(i)