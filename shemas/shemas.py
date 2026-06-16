from pydantic import BaseModel,Field

class WalletBase (BaseModel):
    wallet_id : int
    balance : int = Field(...,ge=0)

class WalletOperation(BaseModel):

    operation_type : str 
    amount : int = Field(...,ge=0)


