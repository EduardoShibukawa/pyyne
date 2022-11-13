
from typing import Final
from src.integration.bank2.bank2_account_transaction import Bank2AccountTransaction
from src.bank.domain.transaction_type import TransactionType


class Bank2TransactionAdapter:

    def __init__(self, bank2_transaction: Bank2AccountTransaction):
        self.__amount__: Final = bank2_transaction.amount
        if bank2_transaction.type == Bank2AccountTransaction.TransactionType.CREDIT:
            self.__type__: Final = TransactionType.CREDIT
        elif bank2_transaction.type == Bank2AccountTransaction.TransactionType.DEBIT:
            self.__type__: Final = TransactionType.DEBIT
        self.__text__: Final = bank2_transaction.text

    def amount(self) -> float:
        return self.__amount__

    def type(self) -> TransactionType:
        return self.__type__

    def text(self) -> str:
        return self.__text__
