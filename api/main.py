from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from python.crud_accounts import update_account
from python.crud_contacts import update_contact
import sqlite3

class AccountUpdate(BaseModel):
    industry: Optional[str] = None
    website: Optional[str] = None
    revenue_in_millions: Optional[float] = None

class ContactUpdate(BaseModel):
    title: Optional[str] = None
    phone: Optional[str] = None
    company_name: Optional[str] = None

from python.crud_accounts import (
    get_all_accounts,
    get_account_by_name,
    update_account
)
from python.crud_contacts import get_contacts_by_company

app = FastAPI(title="CRM API")

@app.get("/")
def health_check():
    return {"status": "CRM API running"}

@app.get("/accounts")
def list_accounts():
    return get_all_accounts()

@app.get("/accounts/{company_name}")
def get_account(company_name: str):
    account = get_account_by_name(company_name)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@app.get("/accounts/{company_name}/contacts")
def get_account_contacts(company_name: str):
    return get_contacts_by_company(company_name)


@app.put("/accounts/{company_name}")
def modify_account(company_name: str, update: AccountUpdate):
    try:
        update_account(
            company_name,
            industry=update.industry,
            website=update.website,
            revenue=update.revenue_in_millions
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": f"Account '{company_name}' updated successfully"}

@app.put("/contacts/{email}")
def modify_contact_endpoint(email: str, update: ContactUpdate):
    try:
        update_contact(
            email,
            title=update.title,
            phone=update.phone,
            company_name=update.company_name
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": f"Contact '{email}' updated successfully"}

@app.get("/analytics/contacts-per-account")
def contacts_per_account():
    conn = sqlite3.connect("crm.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT company_name, contact_count
        FROM contacts_per_account;
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/analytics/accounts-by-industry")
def accounts_by_industry():
    conn = sqlite3.connect("crm.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT industry, account_count
        FROM accounts_by_industry;
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/analytics/top-accounts-by-contacts")
def top_accounts():
    conn = sqlite3.connect("crm.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT company_name, contact_count
        FROM top_accounts_by_contacts;
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows