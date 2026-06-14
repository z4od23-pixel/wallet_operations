from fastapi import APIRouter, HTTPException,status
from sqlalchemy import select
from shemas.shemas import WalletBase,WalletOperation
from models.wallet import WalletMOdel
from database import SessionDep

router = APIRouter(prefix="/api/v1/wallets", tags=["Операции кошелька"])

@router.get("/{wallet_id}")
async def get_balance(wallet_id : int, session : SessionDep)  :
    check_query = select(WalletMOdel)
    check_result = await session.execute(check_query)
    check_id = check_result.scalars().all()
    if len(check_id) < wallet_id :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Кошелек с таким id не найден !')
    
    query = select(WalletMOdel.balance).where(WalletMOdel.wallet_id == wallet_id)
    result = await session.execute(query)
    balance = result.scalars().all()
    return {"Баланс кошелька " :balance[0], " Wallet_id ": wallet_id}

 
