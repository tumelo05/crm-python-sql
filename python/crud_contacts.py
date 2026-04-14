import sqlite3

DB_PATH = "crm.db"


def get_all_contacts():
    """
    Return all contacts in the system.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            name,
            email,
            title,
            phone,
            company_name
        FROM contacts
        ORDER BY name;
    """)

    contacts = cursor.fetchall()
    conn.close()
    return contacts


def get_contact_by_email(email: str):
    """
    Return a single contact identified by email.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            name,
            email,
            title,
            phone,
            company_name
        FROM contacts
        WHERE email = ?;
    """, (email,))

    contact = cursor.fetchone()
    conn.close()
    return contact


def get_contacts_by_company(company_name: str):
    """
    Return all contacts associated with a given company.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            name,
            email,
            title,
            phone
        FROM contacts
        WHERE company_name = ?
        ORDER BY name;
    """, (company_name,))

    contacts = cursor.fetchall()
    conn.close()
    return contacts


def update_contact(
    email: str,
    title: str | None = None,
    phone: str | None = None,
    company_name: str | None = None
):
    """
    Update one or more fields for an existing contact.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    updates = []
    values = []

    if title is not None:
        updates.append("title = ?")
        values.append(title)

    if phone is not None:
        updates.append("phone = ?")
        values.append(phone)

    if company_name is not None:
        updates.append("company_name = ?")
        values.append(company_name)

    if not updates:
        conn.close()
        raise ValueError("No fields provided to update.")

    values.append(email)

    query = f"""
        UPDATE contacts
        SET {', '.join(updates)}
        WHERE email = ?;
    """

    cursor.execute(query, tuple(values))
    conn.commit()
    conn.close()