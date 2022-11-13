from src.integration.bank1.bank1_transaction import Bank1Transaction
from src.bank.domain.transaction_type import TransactionType


class Bank1TransactionAdapter:
    def __init__(self, bank1_transaction: Bank1Transaction):
        self.__transaction__ = bank1_transaction

    def amount(self) -> float:
        return self.__transaction__.amount

    def type(self) -> TransactionType:
        if self.__transaction__.type == 1:
            return TransactionType.CREDIT
        elif self.__transaction__.type == 2:
            return TransactionType.DEBIT

    def text(self) -> str:
        return self.__transaction__.text
