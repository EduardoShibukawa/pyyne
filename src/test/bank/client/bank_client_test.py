from pprint import pprint
import unittest
from src.bank.client.bank_client import BankClient
from src.integration.bank1.bank1_account_source import Bank1AccountSource
from src.integration.bank2.bank2_account_source import Bank2AccountSource
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter
from src.bank.domain.adapter.bank2_balance_adapter import Bank2BalanceAdapter


class PrintBalanceUseCaseTest(unittest.TestCase):

    def setUp(self):
        self.client = BankClient()

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


if __name__ == '__main__':
    unittest.main()
