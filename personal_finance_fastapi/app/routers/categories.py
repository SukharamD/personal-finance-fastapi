from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..deps import get_db, get_current_user

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/add", response_model=schemas.CategoryOut)
def add_category(cat: schemas.CategoryCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.create_category(db, current_user.id, cat)

@router.get("/", response_model=List[schemas.CategoryOut])
def get_categories(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.list_categories(db, current_user.id)
