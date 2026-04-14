import sqlite3

conn = sqlite3.connect("crm.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

with open("sql/views/contacts_per_account.sql") as f:
    cursor.executescript(f.read())

with open("sql/views/accounts_by_industry.sql") as f:
    cursor.executescript(f.read())

with open("sql/views/top_accounts_by_contacts.sql") as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()

print("Analytics views created.")