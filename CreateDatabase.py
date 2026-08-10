import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Anmol@21"
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE testdb")

print("✅ Database created!")

conn.close()