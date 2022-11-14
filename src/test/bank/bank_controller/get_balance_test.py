import unittest
from unittest.mock import MagicMock

from src.bank.bank_controller import BankController


class GetBalanceTest(unittest.TestCase):

    def setUp(self):
        self.get_balance_use_case = MagicMock()
        self.bank_controller = BankController(
            self.get_balance_use_case, MagicMock())

    def test_should_call_get_balance_use_case_once(self):
        self.bank_controller.get_balances(123)
        self.get_balance_use_case.assert_called_once_with(123)


if __name__ == '__main__':
    unittest.main()
