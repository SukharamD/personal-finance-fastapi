from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, categories, transactions, budgets, analytics, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Personal Finance API")

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(transactions.router)
app.include_router(budgets.router)
app.include_router(analytics.router)
app.include_router(reports.router)

@app.get("/")
def root():
    return {"message":"Personal Finance API. Visit /docs for interactive docs."}
