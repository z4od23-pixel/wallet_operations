from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import ForeignKey
from database import Model

class OperationsModel(Model):
    __tablename__ = "operations"

    operation_id : Mapped[int] = mapped_column(primary_key=True, init=False)
    wallet_id : Mapped[int] = mapped_column(ForeignKey("wallets.wallet_id"))
    operation_type : Mapped[str] 
    amount : Mapped[int] 

