import unittest
from unittest.mock import MagicMock

from src.bank.bank_controller import BankController
from src.bank.domain.usecase.get_balance_usecase import GetBalanceUseCase


class GetBalanceTest(unittest.TestCase):

    def setUp(self):
        self.get_balance_use_case = GetBalanceUseCase(MagicMock())
        self.get_balance_use_case.get_account_balance = MagicMock()
        self.bank_controller = BankController(
            self.get_balance_use_case, MagicMock())

    def test_should_call_get_balance_use_case_once(self):
        self.bank_controller.get_balances(123)
        self.get_balance_use_case.get_account_balance.assert_called_once_with(
            123)


if __name__ == '__main__':
    unittest.main()
