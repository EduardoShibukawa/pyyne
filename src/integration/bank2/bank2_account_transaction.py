from enum import Enum


class Bank2AccountTransaction:
    class TransactionType(Enum):
        DEBIT = 1,
        CREDIT = 2

    def __init__(self, amount, type: TransactionType, text):
        self.amount = amount
        self.type = type
        self.text = text
