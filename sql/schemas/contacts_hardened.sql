CREATE TABLE contacts_new (
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL CHECK (email LIKE '%@%'),
    name TEXT NOT NULL,
    phone TEXT,
    title TEXT,
    company_name TEXT NOT NULL,
    FOREIGN KEY (company_name)
        REFERENCES accounts_new(company_name)
        ON DELETE CASCADE
);