from fastapi import APIRouter, HTTPException,status
from sqlalchemy import select, update
from shemas.shemas import WalletBase,WalletOperation
from models.wallet import WalletMOdel
from models.wallet_operations import OperationsModel
from database import SessionDep

router = APIRouter(prefix="/api/v1/wallets", tags=["Кошелек"])

@router.get("/{wallet_id}")
async def get_balance(wallet_id : int, session : SessionDep) -> dict :
    check_query = select(WalletMOdel)
    check_result = await session.execute(check_query)
    check_id = check_result.scalars().all()
    if len(check_id) < wallet_id :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Кошелек с таким id не найден !')
    
    query = select(WalletMOdel.balance).where(WalletMOdel.wallet_id == wallet_id)
    result = await session.execute(query)
    balance = result.scalars().all()
    return {"Баланс кошелька " :balance[0], " Wallet_id ": wallet_id}

@router.post("/{wallet_id}/operation")
async def wallet_operation(wallet_id: int, operation: WalletOperation, session: SessionDep ) :
    check_query = select(WalletMOdel)
    check_result = await session.execute(check_query)
    check_id = check_result.scalars().all()
    if len(check_id) < wallet_id :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Кошелек с таким id не найден !')
    else : 
        if operation.operation_type == "DEPOSIT":
            new_operation = OperationsModel(wallet_id=wallet_id,**operation.model_dump())
            session.add(new_operation)
            await session.commit()
            balance_change = operation.amount
        elif operation.operation_type == "WITHDRAW" :
            new_operation = OperationsModel(wallet_id=wallet_id,**operation.model_dump())
            session.add(new_operation)
            await session.commit()
            balance_change = -operation.amount
        else : 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Неверный тип операции !")
        
        update_balance_query = update(WalletMOdel).where(WalletMOdel.wallet_id == wallet_id).values(balance = WalletMOdel.balance + balance_change )
        await session.execute(update_balance_query)
        await session.commit()

        return "Успешно"






    



 
