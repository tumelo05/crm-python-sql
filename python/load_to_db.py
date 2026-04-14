import pandas as pd
import sqlite3

conn = sqlite3.connect("crm.db")

companies = pd.read_csv("data/curated/clean_companies.csv")
people = pd.read_csv("data/curated/clean_people.csv")

companies.rename(columns={
    "Company_Name": "company_name",
    "Revenue_in_Millions": "revenue_in_millions"
}, inplace=True)


people.rename(columns={
    "Email": "email",
    "Name": "name",
    "Phone_Number": "phone",
    "Title": "title",
    "Company": "company_name"
}, inplace=True)


companies.to_sql("accounts", conn, if_exists="append", index=False)
people.to_sql("contacts", conn, if_exists="append", index=False)

conn.close()

print("Data loaded into database!")