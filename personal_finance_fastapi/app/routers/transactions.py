from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..deps import get_db, get_current_user
import io, csv
from datetime import datetime
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/add", response_model=schemas.TransactionOut)
def add_transaction(tr: schemas.TransactionCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.create_transaction(db, current_user.id, tr)

@router.get("/", response_model=List[schemas.TransactionOut])
def list_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.list_transactions(db, current_user.id, skip, limit)

@router.post("/upload-csv")
def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    content = file.file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(content)
    created = []
    for row in reader:
        try:
            amount = float(row.get("amount") or row.get("Amount"))
            ttype = row.get("type", "expense")
            date_str = row.get("date") or row.get("Date")
            date = datetime.fromisoformat(date_str) if date_str else datetime.utcnow()
            notes = row.get("notes","")
            tr = schemas.TransactionCreate(amount=amount, type=ttype, date=date, notes=notes)
            db_tr = crud.create_transaction(db, current_user.id, tr)
            created.append({"id": db_tr.id, "amount": db_tr.amount})
        except Exception as e:
            # skip malformed rows
            continue
    return JSONResponse({"created": created, "count": len(created)})
