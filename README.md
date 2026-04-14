A production‑style CRM (Customer Relationship Management) backend built locally using Python, SQLite, and FastAPI.
This project demonstrates end‑to‑end backend and data‑engineering fundamentals, including ETL pipelines, relational modeling, REST APIs, analytics, and schema migrations.
The application manages:

Accounts (companies)
Contacts (people associated with companies)
Relationships between them
Analytical insights derived from the data


  Architecture Overview
Raw CSV Data
   │
   ▼
Python ETL (Cleaning & Validation)
   │
   ▼
SQLite Database
   ├── Transactional Tables (Accounts, Contacts)
   ├── Constraints & Indexes
   ├── Analytics Views
   │
   ▼
FastAPI (REST API + Swagger UI)

This mirrors how real CRM systems and data platforms are structured under managed solutions, but is implemented entirely locally to showcase full-stack understanding.

  Key Features
  Data Engineering

CSV ingestion
Data cleaning & normalization
Deduplication
Referential integrity between entities

  Relational Data Model

accounts and contacts tables
Foreign key relationships
Cascading deletes
SQL constraints (NOT NULL, CHECK, UNIQUE)
Indexes for performance

🔹 API Layer (FastAPI)

Read and update endpoints for Accounts and Contacts
Input validation with Pydantic
Auto‑generated OpenAPI / Swagger documentation

Core Endpoints

GET /accounts
GET /accounts/{company_name}
GET /accounts/{company_name}/contacts
PUT /accounts/{company_name}
PUT /contacts/{email}

🔹 Analytics
Analytics are implemented as SQL views and exposed via API endpoints:

Contacts per account
Accounts by industry
Top accounts by number of contacts

Analytics Endpoints

GET /analytics/contacts-per-account
GET /analytics/accounts-by-industry
GET /analytics/top-accounts-by-contacts

🔹 Schema Hardening & Migration

Enforced foreign keys
Data validity constraints
Indexes for join performance
Idempotent schema migration handling dependent SQL views


🚀 Running the Project Locally
1️⃣ Install Dependencies
Shellpip install -r requirements.txtShow more lines
2️⃣ Clean and Load the Data
Shellpython python/clean_data.pypython python/load_to_db.pyShow more lines
3️⃣ Apply Schema Hardening and Analytics
Shellpython python/migrate_schema.pypython python/create_views.py``Show more lines
4️⃣ Start the API Server
Shelluvicorn api.main:app --reloadShow more lines
5️⃣ Open Swagger UI
http://127.0.0.1:8000/docs

This interface allows you to explore and test all API endpoints interactively.

🧪 Example Use Cases

View all companies and their details
Update account or contact information
Retrieve contacts associated with a specific company
Analyze customer distribution by industry
Identify companies with the largest number of contacts


  Tech Stack

Python
SQLite
FastAPI
Pandas
SQL
Pydantic


 Why This Project
This project was built to demonstrate:

Practical backend architecture
SQL data modeling and migrations
ETL pipeline design
REST API development
Analytics layered on top of transactional systems

It is intentionally implemented without managed services to highlight understanding of system internals.

Future Enhancements

Pagination for large datasets
Authentication & authorization
Dockerized deployment
Automated tests
Frontend client


 Author
Tumelo Sethosa
