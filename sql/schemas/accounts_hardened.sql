CREATE TABLE accounts_new (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT UNIQUE NOT NULL,
    website TEXT NOT NULL CHECK (website != ''),
    industry TEXT NOT NULL,
    address TEXT NOT NULL,
    revenue_in_millions REAL NOT NULL CHECK (revenue_in_millions >= 0)
);