import unittest
from datetime import datetime
from src.bank.domain.usecase.get_transactions_usecase import GetTransactionsUseCase
from src.bank.domain.bank_transaction import BankTransaction
from src.bank.domain.transaction_type import TransactionType


class GetBalanceUseCaseTest(unittest.TestCase):

    def test_should_return_transactions(self):
        transactions = [
            BankTransaction(
                100, TransactionType.CREDIT, "Check deposit"),
            BankTransaction(
                25.5, TransactionType.DEBIT, "Debit card purchase"),
            BankTransaction(
                225, TransactionType.DEBIT, "Rent payment"),
            BankTransaction(
                125.0, TransactionType.DEBIT, "Amazon.com"),
            BankTransaction(
                500.0, TransactionType.DEBIT, "Car insurance"),
            BankTransaction(
                800.0, TransactionType.CREDIT, "Salary")
        ]

        def get_transactions(
                account_id, from_date, to_date):
            return transactions

        self.use_case = GetTransactionsUseCase(
            get_transactions
        )

        self.assertEqual(self.use_case.get_transactions(
            123, datetime.today(), datetime.today()), transactions)


if __name__ == '__main__':
    unittest.main()
