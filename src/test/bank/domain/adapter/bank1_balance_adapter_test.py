import unittest
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter


class Bank1BalanceAdapterTest(unittest.TestCase):

    def setUp(self):
        self.bank1_balance_adapter = Bank1BalanceAdapter(10.0, "USD")

    def test_should_have_correctly_balance(self):
        self.assertEqual(self.bank1_balance_adapter.balance(), 10.0)

    def test_should_have_correctly_currency(self):
        self.assertEqual(self.bank1_balance_adapter.currency(), "USD")


if __name__ == '__main__':
    unittest.main()
