from database import Model
from sqlalchemy.orm import Mapped, mapped_column

class WalletMOdel(Model):
    __tablename__ = "operations"

    wallet_id : Mapped[int] = mapped_column(primary_key=True, init=False)
    balance : Mapped[int]
    operation_type : Mapped[str] 
    amount : Mapped[int]