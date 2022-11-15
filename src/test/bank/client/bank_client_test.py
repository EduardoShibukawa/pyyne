import unittest
from datetime import datetime
from unittest.mock import MagicMock


from src.bank.client.bank_client import BankClient
from src.integration.bank1.bank1_account_source import Bank1AccountSource
from src.integration.bank2.bank2_account_source import Bank2AccountSource
from src.integration.bank2.bank2_account_balance import Bank2AccountBalance
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter
from src.bank.domain.adapter.bank2_balance_adapter import Bank2BalanceAdapter
from src.bank.domain.adapter.bank1_transaction_adapter import Bank1TransactionAdapter
from src.bank.domain.adapter.bank2_transaction_adapter import Bank2TransactionAdapter


class BankClientTest(unittest.TestCase):

    def setUp(self):
        self.bank1_account_source = Bank1AccountSource()
        self.bank2_account_source = Bank2AccountSource()
        self.client = BankClient(
            self.bank1_account_source, self.bank2_account_source)

    def test_get_account_balance_should_call_account_source(self):
        self.bank1_account_source.get_account_balance = MagicMock(
            return_value=100.0)
        self.bank1_account_source.get_account_currency = MagicMock(
            return_value="US")
        self.bank2_account_source.get_account_balance = MagicMock(
            return_value=Bank2AccountBalance(100.0, "US")
        )

        self.client.get_account_balance(123)

        self.bank1_account_source.get_account_balance.assert_called_once_with(
            123)
        self.bank1_account_source.get_account_balance.assert_called_once_with(
            123)
        self.bank2_account_source.get_account_balance.assert_called_once_with(
            123)

    def test_get_transactions_should_call_account_source(self):
        self.bank1_account_source.get_transactions = MagicMock(return_value=[])
        self.bank2_account_source.get_transactions = MagicMock(return_value=[])

        self.client.get_transactions(
            123, datetime.today().date(), datetime.today().date())

        self.bank1_account_source.get_transactions.assert_called_once_with(
            123, datetime.today().date(), datetime.today().date())
        self.bank2_account_source.get_transactions.assert_called_once_with(
            123, datetime.today().date(), datetime.today().date())

    def test_should_return_correctly_account_balance(self):
        self.assertEquals(
            self.client.get_account_balance(123),
            [
                Bank1BalanceAdapter(
                    Bank1AccountSource().get_account_balance(123),
                    Bank1AccountSource().get_account_currency(123)
                ),
                Bank2BalanceAdapter(
                    Bank2AccountSource().get_account_balance(123))
            ]
        )

    def test_should_return_correctly_account_transaction(self):
        self.assertEquals(
            self.client.get_transactions(
                123, datetime.today().date(), datetime.today().date()),
            [
                [Bank1TransactionAdapter(t) for t in Bank1AccountSource().get_transactions(
                    123, datetime.today().date(), datetime.today().date())],
                [Bank2TransactionAdapter(t) for t in
                    Bank2AccountSource().get_transactions(123, datetime.today().date(), datetime.today().date())]
            ]
        )


if __name__ == '__main__':
    unittest.main()
