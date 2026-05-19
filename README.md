🚀 CRM Backend (Python, SQL & FastAPI)

A production-style CRM backend demonstrating end-to-end data engineering and backend development — from raw CSV ingestion to analytics served via REST APIs.

This system manages:

Accounts (companies)
Contacts (people)

It supports both transactional operations and analytical insights.

---

📌 Overview

This project showcases how to build a backend system from scratch without relying on external CRM tools.

It covers:

Data ingestion and cleaning (ETL)
Relational database design
SQL-based analytics
REST API development

---

🏗️ Architecture
CSV Data
   ↓
Python ETL (cleaning & validation)
   ↓
SQLite Database
   ↓
SQL Views (analytics layer)
   ↓
FastAPI REST API

---

⚙️ Tech Stack
Python
SQLite
SQL
FastAPI
Pandas
Pydantic

---

🔑 Key Features
CSV ingestion and cleaning pipeline (Pandas + Python)
Data validation and deduplication
Normalized relational schema with:
Foreign keys
Constraints
Indexed queries for performance
REST API with input validation (Pydantic)
SQL-based analytics exposed via API endpoints

---

🗄️ Data Pipeline (ETL)

The ETL layer:

Loads raw CSV data
Cleans inconsistent records
Validates required fields
Removes duplicates
Prepares structured data for insertion
```
python3 python/clean_data.py
python3 python/load_to_db.py
```

---
🧱 Database Layer
SQLite relational database
Normalized schema for accounts and contacts
Indexed columns for faster queries
Schema evolution supported via migrations
```
python3 python/migrate_schema.py
```
---

📊 Analytics Layer

Analytics are implemented using SQL views.

These provide:

Aggregated insights
Precomputed metrics
Efficient querying for API consumption
```
python3 python/create_views.py
```
---

🌐 API Layer (FastAPI)

The API exposes both core CRM operations and analytics endpoints.

▶️ Run the API
```
uvicorn api.main:app --reload
```

📄 Interactive Docs
```
http://127.0.0.1:8000/docs
```
---

📡 API Endpoints
🔹 Core Endpoints
```
GET    /accounts
GET    /accounts/{company_name}
GET    /accounts/{company_name}/contacts
PUT    /accounts/{company_name}
PUT    /contacts/{email}
```
🔹 Analytics Endpoints
```
GET    /analytics/contacts-per-account
GET    /analytics/accounts-by-industry
GET    /analytics/top-accounts-by-contacts
```

---
🛠️ Run Locally
1. Install dependencies
```
pip install -r requirements.txt
```
2. Run ETL pipeline
```
python3 python/clean_data.py
python3 python/load_to_db.py
```
3. Apply migrations & create views
```
python3 python/migrate_schema.py
python3 python/create_views.py
```
4. Start API
```
uvicorn api.main:app --reload
```

---
💡 Example Use Cases
Retrieve and update customer data
Explore company–contact relationships
Analyze customer distribution by industry
Identify high-value accounts by contact volume

---
🎯 Why This Matters

This project demonstrates practical, real-world skills in:

Backend system design
Data modeling and schema evolution
ETL pipeline development
REST API design
SQL-based analytics

Built without external CRM tools to reflect real engineering workflows.
---
👤 Author

Tumelo Sethosa

---
⭐ If you like this project

Give it a star ⭐ on GitHub!
