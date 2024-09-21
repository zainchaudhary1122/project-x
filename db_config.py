import mysql.connector
import os

cnx = mysql.connector.connect(
    user= os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    database=os.getenv('DB_NAME'),
    port=os.getenv('DB_PORT')
)

# Create a cursor object
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM user where id = 1"
cursor.execute(query)

# Fetch results
results = cursor.fetchall()

# Print results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()