import unittest
from src.bank.domain.adapter.bank2_balance_adapter import Bank2BalanceAdapter
from src.integration.bank2.bank2_account_balance import Bank2AccountBalance


class Bank2BalanceAdapterTest(unittest.TestCase):

    def setUp(self):
        self.bank2_account_balance = Bank2AccountBalance(512.5, "USD")
        self.bank2_balance_adapter = Bank2BalanceAdapter(
            self.bank2_account_balance)

    def test_should_have_correctly_balance(self):
        self.assertEqual(self.bank2_balance_adapter.balance(),
                         self.bank2_account_balance.balance)

    def test_should_have_correctly_currency(self):
        self.assertEqual(self.bank2_balance_adapter.currency(),
                         self.bank2_account_balance.currency)

    def test_should_have_default_balance_and_currency_when_null(self):
        self.bank2_balance_adapter = Bank2BalanceAdapter(None)
        self.assertEqual(self.bank2_balance_adapter.balance(),
                         0.00)
        self.assertEqual(self.bank2_balance_adapter.currency(),
                         "USD")

    def test_should_have_default_balance_and_currency_when_balance_is_null(self):
        self.bank2_balance_adapter = Bank2BalanceAdapter(
            Bank2AccountBalance(None, "USD"))
        self.assertEqual(self.bank2_balance_adapter.balance(),
                         0.00)

    def test_should_have_default_balance_and_currency_when_currency_is_null(self):
        self.bank2_balance_adapter = Bank2BalanceAdapter(
            Bank2AccountBalance(10.0, None))
        self.assertEqual(self.bank2_balance_adapter.currency(),
                         "USD")


if __name__ == '__main__':
    unittest.main()
