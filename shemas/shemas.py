from pydantic import BaseModel,Field

class WalletBase (BaseModel):
    balance : int = Field(...,ge=0)

class WalletOperation(WalletBase):
    amount : int = Field(...,ge=0)
    operation_type : str = "DEPOSIT" or "WITHDRAW"