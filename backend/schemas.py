from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class UserCreate(BaseModel):
    telegram_id: int
    username: Optional[str]
    full_name: Optional[str]

class TransactionCreate(BaseModel):
    type: TransactionType
    amount: float
    description: Optional[str] = None
