from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum



Base = declarative_base()

class TransactionType(str, enum.Enum):
    income = "income"
    expense = "expense"

class User(Base):
    __tablename__ = "users"
    
    id = Column(BigInteger, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    username = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now())

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger)
    type = Column(Enum(TransactionType))
    amount = Column(Float)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
