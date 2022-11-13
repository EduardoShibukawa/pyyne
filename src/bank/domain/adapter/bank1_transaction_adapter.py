from src.integration.bank1.bank1_transaction import Bank1Transaction
from src.bank.domain.transaction_type import TransactionType


class Bank1TransactionAdapter:
    def __init__(self, bank1_transaction: Bank1Transaction):
        self.transaction = bank1_transaction

    def amount(self) -> float:
        return self.transaction.amount

    def type(self) -> TransactionType:
        if self.transaction.type == 1:
            return TransactionType.CREDIT
        elif self.transaction.type == 2:
            return TransactionType.DEBIT

    def text(self):
        return self.transaction.text
