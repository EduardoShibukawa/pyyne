from enum import Enum


class Bank2AccountTransaction:
    class TransactionType(Enum):
        DEBIT = 1,
        CREDIT = 2

    def __init__(self, amount, type: TransactionType, text):
        self.amount = amount
        self.type = type
        self.text = text

    def __repr__(self):
        details = '{'
        details += f'"amount"  : {self.amount},'
        details += f'"type": "{self.type}",'
        details += f'"text": "{self.text}"'
        details += '}'

        return details
