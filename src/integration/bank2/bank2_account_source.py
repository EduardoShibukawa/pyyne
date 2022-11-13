from integration.bank2.bank2_account_transaction import Bank2AccountTransaction
from bank2_account_balance import Bank2AccountBalance


class Bank2AccountSource:
    def get_account_balance(self, account_id):
        return Bank2AccountBalance(512.5, "USD")

    def get_transactions(account_id, from_date, to_date):
        return [
            Bank2AccountTransaction(
                125.0, Bank2AccountTransaction.TransactionType.DEBIT, "Amazon.com"),
            Bank2AccountTransaction(
                500.0, Bank2AccountTransaction.TransactionType.DEBIT, "Car insurance"),
            Bank2AccountTransaction(
                800.0, Bank2AccountTransaction.TransactionType.CREDIT, "Salary")
        ]
