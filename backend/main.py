from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas, crud, database
from fastapi.middleware.cors import CORSMiddleware






app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*","https://526b-2a05-45c2-73f2-cc00-a326-acf7-3d8a-a26d.ngrok-free.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.post("/user/")
async def create_or_get_user(user: schemas.UserCreate, db: AsyncSession = Depends(database.get_db)):
    db_user = await crud.get_user_by_telegram_id(db, user.telegram_id)
    if db_user:
        result = await crud.get_transactions(db, user_id=db_user.telegram_id)
        return result
    
    createUser = await crud.create_user(db, user)
    if not createUser:
        raise HTTPException(status_code=400, detail="User creation failed")
    result = await crud.get_transactions(db, user_id=createUser.telegram_id)
    return result

@app.post("/transaction/{telegram_id}")
async def add_transaction(transaction: schemas.TransactionCreate, telegram_id: int, db: AsyncSession = Depends(database.get_db)):
    print(telegram_id, transaction.dict())
    db_user = await crud.get_user_by_telegram_id(db, telegram_id)
    

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.create_transaction(db, db_user.id, transaction)

@app.get("/data/user/{telegram_id}")
async def get_transactions(telegram_id: int, db: AsyncSession = Depends(database.get_db)):
    db_user = await crud.get_user_by_telegram_id(db, telegram_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    result = await crud.get_transactions(db, user_id=db_user.telegram_id)
    print(1111)
    return result
