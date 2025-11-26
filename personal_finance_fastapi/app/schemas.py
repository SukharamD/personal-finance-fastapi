from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime, date

class UserCreate(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserOut(BaseModel):
    id: int
    name: Optional[str]
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class CategoryCreate(BaseModel):
    name: str
    type: Optional[str] = "expense"

class CategoryOut(BaseModel):
    id: int
    name: str
    type: str
    class Config:
        orm_mode = True

class TransactionCreate(BaseModel):
    amount: float
    type: str
    date: Optional[datetime] = None
    category_id: Optional[int] = None
    notes: Optional[str] = None

class TransactionOut(BaseModel):
    id: int
    amount: float
    type: str
    date: datetime
    notes: Optional[str]
    category: Optional[CategoryOut]
    class Config:
        orm_mode = True

class BudgetCreate(BaseModel):
    category_id: int
    monthly_limit: float

class BudgetOut(BaseModel):
    id: int
    category_id: int
    monthly_limit: float
    class Config:
        orm_mode = True
