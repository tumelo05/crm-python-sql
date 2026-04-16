CRM Backend (Python, SQL & FastAPI)
This project is a production‑style Customer Relationship Management (CRM) backend system built locally using Python, SQLite, and FastAPI.
It demonstrates end‑to‑end backend and data‑engineering principles, from raw data ingestion to analytics exposed via REST APIs.
The system manages Accounts (companies) and Contacts (people associated with companies) and supports both transactional operations and analytical insights.

Architecture Overview
Raw CSV Data
   │
   ▼
Python ETL (Cleaning & Validation)
   │
   ▼
SQLite Relational Database
   ├── Accounts & Contacts tables
   ├── Constraints & Indexes
   ├── SQL Analytics Views
   │
   ▼
FastAPI (REST API + Swagger UI)

This architecture mirrors how real CRM and analytics systems are implemented in production, with a clear separation between data preparation, storage, business logic, and analytics.

Key Features
Data Engineering

CSV data ingestion
Data cleaning and normalization
Deduplication and validation
Curated datasets for downstream use

Relational Data Model

accounts and contacts tables
Foreign‑key relationships
Cascading deletes
Enforced constraints (NOT NULL, CHECK, UNIQUE)
Indexes for query performance

API Layer (FastAPI)

RESTful endpoints with correct HTTP semantics
Input validation using Pydantic
Auto‑generated OpenAPI / Swagger documentation

Core Endpoints

GET /accounts
GET /accounts/{company_name}
GET /accounts/{company_name}/contacts
PUT /accounts/{company_name}
PUT /contacts/{email}

Analytics
Analytics are implemented as SQL views and exposed via API endpoints:

Contacts per account
Accounts by industry
Top accounts by number of contacts

Analytics Endpoints

GET /analytics/contacts-per-account
GET /analytics/accounts-by-industry
GET /analytics/top-accounts-by-contacts


Running the Project Locally
1. Install Dependencies
pip install -r requirements.txt
2. Clean and Load the Data
python3 python/clean_data.py python3 python/load_to_db.py
3. Apply Schema Hardening and Analytics
python3 python/migrate_schema.py python3 python/create_views.py
4. Start the API Server
uvicorn api.main:app --reload
5. Open Swagger UI
http://127.0.0.1:8000/docs

This interface allows interactive exploration and testing of all API endpoints.

Example Use Cases

View all customer accounts
Update account or contact information
Retrieve contacts associated with a specific company
Analyze customer distribution by industry
Identify top accounts by contact volume


Technology Stack

Python
SQLite
SQL
FastAPI
Pandas
Pydantic
Git & GitHub


Why This Project
This project was intentionally built without managed CRM platforms to demonstrate:

Backend system design
Data modeling and schema evolution
ETL pipelines and data validation
REST API development
Analytical query design
End‑to‑end data‑engineering thinking

It reflects real‑world backend and data‑engineering workflows rather than framework‑heavy abstractions.

Author
Tumelo Sethosa
