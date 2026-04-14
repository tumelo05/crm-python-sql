import sqlite3

conn = sqlite3.connect("crm.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    a.company_name,
    c.name,
    c.email,
    c.title
FROM accounts a
LEFT JOIN contacts c
ON a.company_name = c.company_name
LIMIT 10;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()