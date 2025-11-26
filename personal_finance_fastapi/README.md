# Personal Finance & Budgeting System (FastAPI)

## Quickstart (development)

1. Create virtual env:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Open docs: http://127.0.0.1:8000/docs

This scaffold uses SQLite for simplicity and includes:
- JWT auth (register/login)
- Transactions (income/expense)
- Categories
- Budgets
- Simple analytics endpoints
- CSV upload for transactions
- Monthly PDF report generation (ReportLab)
