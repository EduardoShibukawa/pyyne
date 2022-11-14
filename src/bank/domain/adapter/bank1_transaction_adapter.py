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

    def __hash__(self):
        return hash(self.__amount__, self.__type__, self.__text__)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.__amount__ == other.__amount__ and
            self.__type__ == other.__type__ and
            self.__text__ == other.__text__
        )

    def __repr__(self):
        details = '{'
        details += f'"amount"  : {self.__amount__},'
        details += f'"type": "{self.__type__}",'
        details += f'"text": "{self.__text__}"'
        details += '}'

        return details
