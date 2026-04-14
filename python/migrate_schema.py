import sqlite3

conn = sqlite3.connect("crm.db")
conn.execute("PRAGMA foreign_keys = OFF;")
cursor = conn.cursor()

# Drop analytics views first
cursor.execute("DROP VIEW IF EXISTS contacts_per_account;")
cursor.execute("DROP VIEW IF EXISTS accounts_by_industry;")
cursor.execute("DROP VIEW IF EXISTS top_accounts_by_contacts;")

# Drop leftover temp tables from previous failed runs
cursor.execute("DROP TABLE IF EXISTS contacts_new;")
cursor.execute("DROP TABLE IF EXISTS accounts_new;")

# Create new hardened tables
with open("sql/schemas/accounts_hardened.sql") as f:
    cursor.executescript(f.read())

with open("sql/schemas/contacts_hardened.sql") as f:
    cursor.executescript(f.read())

# Copy data from old tables into new tables
cursor.execute("""
INSERT INTO accounts_new (company_name, website, industry, address, revenue_in_millions)
SELECT company_name, website, industry, address, revenue_in_millions
FROM accounts;
""")

cursor.execute("""
INSERT INTO contacts_new (email, name, phone, title, company_name)
SELECT email, name, phone, title, company_name
FROM contacts;
""")

# Remove old tables
cursor.execute("DROP TABLE contacts;")
cursor.execute("DROP TABLE accounts;")

# Rename new tables
cursor.execute("ALTER TABLE accounts_new RENAME TO accounts;")
cursor.execute("ALTER TABLE contacts_new RENAME TO contacts;")

conn.commit()
conn.close()

print("Schema hardened successfully.")