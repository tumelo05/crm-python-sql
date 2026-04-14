import sqlite3

DB_PATH = "crm.db"

def get_all_accounts():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT company_name, industry, website, address, revenue_in_millions
        FROM accounts
        ORDER BY company_name;
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_account_by_name(company_name):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT company_name, industry, website, address, revenue_in_millions
        FROM accounts
        WHERE company_name = ?;
    """, (company_name,))
    row = cursor.fetchone()
    conn.close()
    return row


def update_account(company_name, industry=None, website=None, revenue=None):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    updates = []
    values = []

    if industry is not None:
        updates.append("industry = ?")
        values.append(industry)

    if website is not None:
        updates.append("website = ?")
        values.append(website)

    if revenue is not None:
        updates.append("revenue_in_millions = ?")
        values.append(revenue)

    if not updates:
        conn.close()
        raise ValueError("No fields provided to update")

    values.append(company_name)

    query = f"""
        UPDATE accounts
        SET {', '.join(updates)}
        WHERE company_name = ?;
    """

    cursor.execute(query, tuple(values))
    conn.commit()
    conn.close()