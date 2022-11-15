import unittest
from unittest.mock import MagicMock

from src.bank.client.bank_client import BankClient
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter
from src.bank.domain.adapter.bank2_balance_adapter import Bank2BalanceAdapter
from src.integration.bank2.bank2_account_balance import Bank2AccountBalance


class BankClientTest(unittest.TestCase):

    def setUp(self):
        self.bank1_account_source = MagicMock()
        self.bank2_account_source = MagicMock()
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

    def test_should_return_correctly_account_balance(self):
        self.bank1_account_source.get_account_balance = MagicMock(
            return_value=100.0)
        self.bank1_account_source.get_account_currency = MagicMock(
            return_value="US")
        self.bank2_account_source.get_account_balance = MagicMock(
            return_value=Bank2AccountBalance(101.11, "US")
        )

        self.assertEquals(
            self.client.get_account_balance(123),
            [
                Bank1BalanceAdapter(103, "US"),
                Bank2BalanceAdapter(Bank2AccountBalance(101.11, "US"))
            ]
        )


if __name__ == '__main__':
    unittest.main()
