from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas, crud, database


app = FastAPI()

@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.post("/user/")
async def create_or_get_user(user: schemas.UserCreate, db: AsyncSession = Depends(database.get_db)):
    db_user = await crud.get_user_by_telegram_id(db, user.telegram_id)
    if db_user:
        return db_user
    return await crud.create_user(db, user)

@app.post("/transaction/")
async def add_transaction(transaction: schemas.TransactionCreate, telegram_id: int, db: AsyncSession = Depends(database.get_db)):
    db_user = await crud.get_user_by_telegram_id(db, telegram_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.create_transaction(db, db_user.id, transaction)
