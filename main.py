import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",        # or your server IP
    user="root",             # MySQL username
    password="kiumbekipya100%",  # MySQL password
    database="attendance_db"   # Database name
)

cursor = connection.cursor()

# Example Query: List tables in the database
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

for table in tables:
    print(table)

# Close connection
cursor.close()
connection.close()
