from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def get_user_by_telegram_id(db: AsyncSession, telegram_id: int):
    result = await db.execute(select(models.User).where(models.User.telegram_id == telegram_id))
    return result.scalars().first()

async def get_transactions(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.Transaction).where(models.Transaction.user_id == user_id))
    return result.scalars().all()

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(
        telegram_id=user.telegram_id,
        username=user.username,
        full_name=user.full_name,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def create_transaction(db: AsyncSession, user_id: int, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        user_id=user_id,
        type=transaction.type,
        amount=transaction.amount,
        description=transaction.description
    )
    db.add(db_transaction)
    await db.commit()
    await db.refresh(db_transaction)
    return db_transaction
