import sqlite3

conn = sqlite3.connect("crm.db")
cursor = conn.cursor()

# Accounts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT UNIQUE NOT NULL,
    website TEXT,
    industry TEXT,
    address TEXT,
    revenue_in_millions REAL
);
""")

# Contacts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    name TEXT,
    phone TEXT,
    title TEXT,
    company_name TEXT,
    FOREIGN KEY (company_name) REFERENCES accounts(company_name)
);
""")

conn.commit()
conn.close()

print("Tables created successfully!")