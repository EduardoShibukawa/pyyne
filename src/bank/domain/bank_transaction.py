from typing import Final
from src.bank.domain.transaction_type import TransactionType


class BankTransaction:

    def __init__(self, amount: float, type: TransactionType, text: str):
        self.__amount__: Final = amount
        self.__type__: Final = type
        self.__text__: Final = text

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
        details += f'Amount  : {self.__amount__}\n'
        details += f'Type         : {self.__type__}\n'
        details += f'Text         : {self.__text__}\n'
        details += '}'

        return details
