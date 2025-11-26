Personal Finance & Budgeting System (FastAPI)

A complete backend system for tracking income, expenses, budgets, analytics, and automated financial reporting — built using FastAPI, PostgreSQL/SQLite, JWT authentication, and ReportLab for PDF generation.

🚀 Features

1. Authentication
- JWT-based login & registration
- Password hashing (bcrypt / argon2)
- Secure token validation

2. Categories
- Create categories (income/expense)
- List all categories
- Soft delete support

3. Transactions
- Add income/expense
- Filter & list transactions
- CSV upload (bulk import)
- Automatic date parsing

4. Budgets
- Set monthly category-wise budgets
- Budget usage tracking
- Threshold alert system (via background tasks – optional)

5. Analytics
- Monthly summary
- Total income & expenses
- Category-wise spending breakdown

6. Reports
- Generate monthly PDF reports
- Stored in reports/ directory
- Download directly from API

7. Architecture
- Modular folder structure
- SQLAlchemy ORM models
- Pydantic v2 schemas

🛠 Tech Stack
- FastAPI (async API framework)
- SQLAlchemy 2.0 (ORM)
- PostgreSQL or SQLite
- ReportLab (PDF generation)
- Pydantic v2
- Uvicorn
- Passlib (password hashing)
- Redis + Celery (optional for background jobs)

  📁 Project Structure
  app/
 ├── routers/
 │    ├── auth.py
 │    ├── categories.py
 │    ├── transactions.py
 │    ├── budgets.py
 │    ├── analytics.py
 │    └── reports.py
 ├── models.py
 ├── schemas.py
 ├── database.py
 ├── security.py
 ├── crud.py
 ├── deps.py
 └── main.py

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/personal-finance-fastapi.git
cd personal-finance-fastapi

2. Create virtual environment
python -m venv env
source env/bin/activate        # Linux/Mac
env\Scripts\activate           # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the server
uvicorn app.main:app --reload

5. Open API documentation
http://127.0.0.1:8000/docs

🗄️ Database Configuration
SQLite (default)
No setup required.

PostgreSQL (optional)
Update database.py:
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/finance_db"

Then create DB:
createdb finance_db

🔐 Authentication Flow

* Register → /auth/register
* Login → /auth/login
* Copy access_token
* Add it to Authorization → Bearer Token in Postman

📌 API Endpoints Summary
***Auth***
- Method	    |  Endpoint	      |    Description
- POST	    |  /auth/register   |  Register new user
- POST	    |  /auth/login      |	Login & get JWT

Categories
* | POST | /categories/add | Add category |
* | GET | /categories/ | List categories |

Transactions
* | POST | /transactions/add | Add transaction |
* | GET | /transactions/ | List transactions |
* | POST | /transactions/upload-csv | Import CSV |

Budgets
* | POST | /budgets/set | Set monthly budget |
* | GET | /budgets/ | List budgets |

Analytics
* | GET | /analytics/summary | Monthly financial summary |

Reports
* | POST | /reports/monthly | Generate & download PDF |
* | POST | /reports/monthly | Generate & download PDF |
