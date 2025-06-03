from pathlib import Path
import sqlite3
# Define the root directory as the folder where this script is located
ROOT_DIR = Path(__file__).parent
# Set the database file name
DB_NAME = 'db.sqlite3'
# Full path to the database file
DB_FILE = ROOT_DIR / DB_NAME
# Name of the table to be created
TABLE_NAME = 'customers'
# Connect to the SQLite database (creates the file if it doesn't exist)
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
# SQL: Create a table if it doesn't exist
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # auto-incrementing unique ID
    'name TEXT UNIQUE,'                             # customer's name as text
    'weight REAL'                            # customer's weight as a decimal number
    ')'
)
# Save the changes
connection.commit()

sql = (
    f'INSERT OR REPLACE INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?,?)'
)

# cursor.execute(sql, ["Maykon", 93])
cursor.executemany(sql, [['Maykon', 93], ['Cibele', 42], ['Magno', 80], ['Maira', 45]])
connection.commit()

# Close the connection
cursor.close()
connection.close()
