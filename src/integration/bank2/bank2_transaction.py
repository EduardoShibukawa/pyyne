from enum import Enum


class Bank2Transaction:
    class TransactionType(Enum):
        DEBIT = 1,
        CREDIT = 2

    def __init__(self, amount, type, text):
        self.amount = amount
        self.type = type
        self.text = text
