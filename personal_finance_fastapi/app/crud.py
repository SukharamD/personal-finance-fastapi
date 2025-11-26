from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from typing import List

# Users
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email==email).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(email=user.email, name=user.name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Categories
def create_category(db: Session, user_id: int, cat: schemas.CategoryCreate):
    db_cat = models.Category(user_id=user_id, name=cat.name, type=cat.type)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def list_categories(db: Session, user_id: int):
    return db.query(models.Category).filter(models.Category.user_id==user_id, models.Category.is_active==True).all()

# Transactions
def create_transaction(db: Session, user_id: int, tr: schemas.TransactionCreate):
    date = tr.date or datetime.utcnow()
    db_tr = models.Transaction(
        user_id=user_id,
        category_id=tr.category_id,
        amount=tr.amount,
        type=tr.type,
        date=date,
        notes=tr.notes
    )
    db.add(db_tr)
    db.commit()
    db.refresh(db_tr)
    return db_tr

def list_transactions(db: Session, user_id: int, skip: int=0, limit: int=100):
    return db.query(models.Transaction).filter(models.Transaction.user_id==user_id).order_by(models.Transaction.date.desc()).offset(skip).limit(limit).all()

# Budgets
def set_budget(db: Session, user_id: int, budget: schemas.BudgetCreate):
    db_b = models.Budget(user_id=user_id, category_id=budget.category_id, monthly_limit=budget.monthly_limit)
    db.add(db_b)
    db.commit()
    db.refresh(db_b)
    return db_b

def get_budgets(db: Session, user_id: int):
    return db.query(models.Budget).filter(models.Budget.user_id==user_id).all()
