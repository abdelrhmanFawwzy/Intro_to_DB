import mysql.connector

conobj = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

cursor = conobj.cursor()
try: 
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
except mysql.connector.Error as err:
    print(f"Failed creating database: {err}")
print("Database 'alx_book_store' created successfully!")
