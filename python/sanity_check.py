import sqlite3

conn = sqlite3.connect("crm.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

cursor.execute("SELECT * FROM contacts_per_account LIMIT 5;")
print(cursor.fetchall())

cursor.execute("SELECT * FROM accounts_by_industry;")
print(cursor.fetchall())

conn.close()