import sqlite3

conn = sqlite3.connect("crm.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS contacts;")
cursor.execute("DROP TABLE IF EXISTS accounts;")

conn.commit()
conn.close()

print("Database reset.")
