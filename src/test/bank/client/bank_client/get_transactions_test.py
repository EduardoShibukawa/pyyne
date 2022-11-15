import unittest
from datetime import datetime
from unittest.mock import MagicMock

from src.bank.client.bank_client import BankClient
from src.bank.domain.adapter.bank1_transaction_adapter import \
    Bank1TransactionAdapter
from src.bank.domain.adapter.bank2_transaction_adapter import \
    Bank2TransactionAdapter
from src.integration.bank1.bank1_transaction import Bank1Transaction
from src.integration.bank2.bank2_account_transaction import \
    Bank2AccountTransaction


class BankClientGetTransactionsTest(unittest.TestCase):

    def setUp(self):
        self.bank1_account_source = MagicMock()
        self.bank2_account_source = MagicMock()
        self.client = BankClient(
            self.bank1_account_source, self.bank2_account_source)

    def test_get_transactions_should_call_account_source(self):
        self.bank1_account_source.get_transactions = MagicMock(return_value=[])
        self.bank2_account_source.get_transactions = MagicMock(return_value=[])

        self.client.get_transactions(
            123, datetime.today().date(), datetime.today().date())

        self.bank1_account_source.get_transactions.assert_called_once_with(
            123, datetime.today().date(), datetime.today().date())
        self.bank2_account_source.get_transactions.assert_called_once_with(
            123, datetime.today().date(), datetime.today().date())

    def test_should_return_correctly_account_transaction(self):
        bank1_transactions = [
            Bank1Transaction(10.0, Bank1Transaction.TYPE_CREDIT,
                             "Bank1Transaction 1"),
            Bank1Transaction(20.0, Bank1Transaction.TYPE_DEBIT,
                             "Bank1Transaction 2")
        ]
        bank2_transactions = [
            Bank2AccountTransaction(
                30.0, Bank2AccountTransaction.TransactionType.DEBIT, "Bank2AccountTransaction 1"),
            Bank2AccountTransaction(
                40.0, Bank2AccountTransaction.TransactionType.CREDIT, "Bank2AccountTransaction 2"),
        ]

        self.bank1_account_source.get_transactions = MagicMock(
            return_value=bank1_transactions)
        self.bank2_account_source.get_transactions = MagicMock(
            return_value=bank2_transactions)

        self.assertEqual(
            self.client.get_transactions(
                123, datetime.today().date(), datetime.today().date()),
            [
                [Bank1TransactionAdapter(t) for t in bank1_transactions],
                [Bank2TransactionAdapter(t) for t in bank2_transactions]
            ]
        )


if __name__ == '__main__':
    unittest.main()
