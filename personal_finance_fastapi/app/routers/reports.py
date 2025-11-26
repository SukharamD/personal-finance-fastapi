from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from ..deps import get_db, get_current_user
from .. import models
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os
from ..config import REPORTS_DIR

router = APIRouter(prefix="/reports", tags=["reports"])
os.makedirs(REPORTS_DIR, exist_ok=True)

def generate_monthly_pdf(user, transactions, out_path):
    c = canvas.Canvas(out_path, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height-50, f"Monthly Report for {user.email}")
    c.setFont("Helvetica", 12)
    y = height - 80
    total_income = sum(t.amount for t in transactions if t.type=="income")
    total_expense = sum(t.amount for t in transactions if t.type!="income")
    c.drawString(50, y, f"Generated: {datetime.utcnow().isoformat()}")
    y -= 20
    c.drawString(50, y, f"Total Income: {total_income:.2f}")
    y -= 20
    c.drawString(50, y, f"Total Expense: {total_expense:.2f}")
    y -= 30
    c.drawString(50, y, "Transactions:")
    y -= 20
    for t in transactions[:50]:
        text = f"{t.date.date().isoformat()} | {t.type} | {t.amount} | {t.category.name if t.category else 'N/A'} | {t.notes or ''}"
        c.drawString(50, y, text[:90])
        y -= 15
        if y < 80:
            c.showPage()
            y = height - 50
    c.save()

@router.post("/monthly")
def create_monthly_report(background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # simple: all transactions this month
    now = datetime.utcnow()
    start_month = datetime(now.year, now.month, 1)
    transactions = db.query(models.Transaction).filter(models.Transaction.user_id==current_user.id, models.Transaction.date >= start_month).order_by(models.Transaction.date.desc()).all()
    filename = f"report_{current_user.id}_{now.year}_{now.month}.pdf"
    out_path = os.path.join(REPORTS_DIR, filename)
    # generate synchronously but can use background_tasks
    generate_monthly_pdf(current_user, transactions, out_path)
    return FileResponse(out_path, media_type="application/pdf", filename=filename)
