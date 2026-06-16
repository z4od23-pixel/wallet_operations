from database import Model
from sqlalchemy.orm import Mapped, mapped_column

class WalletMOdel(Model):
    __tablename__ = "wallets"

    wallet_id : Mapped[int] = mapped_column(primary_key=True, init=False)
    balance : Mapped[int]
