from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..deps import get_db, get_current_user
from .. import models
from datetime import datetime, timedelta
from collections import defaultdict

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/summary")
def summary(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # simple summary: total income, total expense, by category totals for current month
    now = datetime.utcnow()
    start_month = datetime(now.year, now.month, 1)
    transactions = db.query(models.Transaction).filter(models.Transaction.user_id==current_user.id, models.Transaction.date >= start_month).all()
    totals = {"income":0.0, "expense":0.0}
    by_category = defaultdict(float)
    for t in transactions:
        if t.type=="income":
            totals["income"] += t.amount
        else:
            totals["expense"] += t.amount
        if t.category:
            by_category[t.category.name] += t.amount
    return {"month_start": start_month.isoformat(), "totals": totals, "by_category": dict(by_category)}
