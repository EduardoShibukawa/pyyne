from typing import Final
from src.integration.bank1.bank1_transaction import Bank1Transaction
from src.bank.domain.transaction_type import TransactionType


class Bank1TransactionAdapter:

    def __init__(self, bank1_transaction: Bank1Transaction):
        self.__amount__: Final = bank1_transaction.amount
        if bank1_transaction.type == 1:
            self.__type__: Final = TransactionType.CREDIT
        elif bank1_transaction.type == 2:
            self.__type__: Final = TransactionType.DEBIT
        self.__text__: Final = bank1_transaction.text

    def amount(self) -> float:
        return self.__amount__

    def type(self) -> TransactionType:
        return self.__type__

    def text(self) -> str:
        return self.__text__
