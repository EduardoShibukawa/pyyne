import unittest
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter


class Bank1BalanceAdapterTest(unittest.TestCase):

    def setUp(self):
        self.bank1_balance_adapter = Bank1BalanceAdapter(10.0, "USD")

    def test_should_have_correctly_balance(self):
        self.assertEqual(self.bank1_balance_adapter.balance(), 10.0)

    def test_should_have_correctly_currency(self):
        self.assertEqual(self.bank1_balance_adapter.currency(), "USD")

    def test_should_have_default_balance_when_null(self):
        self.bank1_balance_adapter = Bank1BalanceAdapter(None, "USD")
        self.assertEqual(self.bank1_balance_adapter.balance(), 0)

    def test_should_have_default_currency_when_null(self):
        self.bank1_balance_adapter = Bank1BalanceAdapter(10.0, None)
        self.assertEqual(self.bank1_balance_adapter.currency(), "USD")


if __name__ == '__main__':
    unittest.main()
