CRM Backend (Python, SQL & FastAPI)

A production-style CRM backend that demonstrates end-to-end data engineering and backend development, from raw CSV ingestion to analytics served via REST APIs.

Manages accounts (companies) and contacts (people) with both transactional operations and analytical insights.

Architecture
CSV Data → Python ETL → SQLite → SQL Views → FastAPI API
ETL layer: cleans, validates, and deduplicates raw data
Database: relational schema with constraints and indexes
Analytics: SQL views for aggregated insights
API: FastAPI service with auto-documented endpoints
Key Features
Data ingestion and cleaning pipeline (Pandas + Python)
Normalized relational schema with foreign keys and constraints
Indexed queries for performance
REST API with input validation (Pydantic)
Built-in analytics exposed via endpoints
API Overview
Core
GET    /accounts
GET    /accounts/{company_name}
GET    /accounts/{company_name}/contacts
PUT    /accounts/{company_name}
PUT    /contacts/{email}
Analytics
GET /analytics/contacts-per-account
GET /analytics/accounts-by-industry
GET /analytics/top-accounts-by-contacts

Interactive docs available at:
http://127.0.0.1:8000/docs

Run Locally
pip install -r requirements.txt

python3 python/clean_data.py
python3 python/load_to_db.py

python3 python/migrate_schema.py
python3 python/create_views.py

uvicorn api.main:app --reload
Example Use Cases
Retrieve and update customer data
Explore company-contact relationships
Analyze customer distribution by industry
Identify high-value accounts by contact volume
Tech Stack

Python • SQLite • SQL • FastAPI • Pandas • Pydantic

Why This Matters

This project shows practical skills in:

Backend system design
Data modeling and schema evolution
ETL pipeline development
REST API design
SQL-based analytics

Built without external CRM tools to reflect real-world engineering workflows.

Author

Tumelo Sethosa
