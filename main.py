from models.wallet import WalletMOdel
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine, Model
from router.router import router as wallet_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    
    print("База данных готова к работе")
    
    yield 
    
    print("Выключение сервера")


app = FastAPI(lifespan=lifespan)
app.include_router(wallet_router)
