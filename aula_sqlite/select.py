import sqlite3

from main import DB_FILE, TABLE_NAME

# Connect to the SQLite database
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Execute a query to select all rows from the table
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

# Iterate over all the rows and print each one
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print()
# Execute a query to select the row with id = 3
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)


# Close the cursor and the connection
cursor.close()
connection.close()
