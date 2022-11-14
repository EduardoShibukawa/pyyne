from typing import Protocol
from src.bank.domain.transaction_type import TransactionType


class Transactionable(Protocol):

    def amount(self) -> float: pass
    def type(self) -> TransactionType: pass
    def text(self) -> str: pass
