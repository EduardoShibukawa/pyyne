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


if __name__ == '__main__':
    unittest.main()
