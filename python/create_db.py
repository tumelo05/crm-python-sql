import sqlite3

# Create (or open) the database file
conn = sqlite3.connect("crm.db")

print("Database created successfully!")

conn.close()
