import pymysql

#  Connect to MySQL
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Anmol@21",
    database="testdb"
)

cursor = conn.cursor()

#  Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

print(" Connected to database & Table ready!")

#  Menu-driven program
while True:
    print("\n===== MENU =====")
    print("1. Insert Data")
    print("2. View Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    #  Insert
    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
        cursor.execute(sql, (name, age))
        conn.commit()

        print(" Data inserted!")

    # ➤ View
    elif choice == 2:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        print("\n Student Data:")
        for row in rows:
            print(row)

    # ➤ Update
    elif choice == 3:
        id = int(input("Enter ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))

        sql = "UPDATE students SET name=%s, age=%s WHERE id=%s"
        cursor.execute(sql, (name, age, id))
        conn.commit()

        print(" Data updated!")

    # ➤ Delete
    elif choice == 4:
        id = int(input("Enter ID to delete: "))

        sql = "DELETE FROM students WHERE id=%s"
        cursor.execute(sql, (id,))
        conn.commit()

        print(" Data deleted!")

    # ➤ Exit
    elif choice == 5:
        print(" Exiting program...")
        break

    else:
        print(" Invalid choice!")

#  Close connection
conn.close()
print(" Connection closed!")