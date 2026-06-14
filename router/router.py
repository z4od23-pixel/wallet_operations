from fastapi import APIRouter
from sqlalchemy import select
from shemas.shemas import WalletBase,WalletOperation
from models.wallet import WalletMOdel
from database import SessionDep

router = APIRouter(prefix="/api/v1/wallets", tags=["Операции кошелька"])

@router.get("/{wallet_id}")
async def get_balance(wallet_id : int, session : SessionDep) ->int :
    query = select(WalletMOdel.balance).where(WalletMOdel.wallet_id==wallet_id)
    result = await session.execute(query)
    balance = result.scalars().all()
    return balance[0]

