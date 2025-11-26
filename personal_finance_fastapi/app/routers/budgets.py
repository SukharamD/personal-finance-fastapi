from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..deps import get_db, get_current_user

router = APIRouter(prefix="/budgets", tags=["budgets"])

@router.post("/set", response_model=schemas.BudgetOut)
def set_budget(b: schemas.BudgetCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.set_budget(db, current_user.id, b)

@router.get("/", response_model=List[schemas.BudgetOut])
def list_budgets(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.get_budgets(db, current_user.id)
