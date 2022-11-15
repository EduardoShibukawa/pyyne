import unittest

from src.bank.domain.bank_balance import BankBalance
from src.bank.domain.usecase.get_balance_usecase import GetBalanceUseCase


class GetBalanceUseCaseTest(unittest.TestCase):

    def test_should_sum_balance(self):
        def get_account_balance_account_bank(
                account_id):
            return [
                BankBalance(100, "RS"),
                BankBalance(200, "RS")
            ]

        self.use_case = GetBalanceUseCase(
            get_account_balance_account_bank
        )

        self.assertEqual(self.use_case.get_account_balance(
            "123"), BankBalance(300, "RS"))

    def test_should_return_default_balance_when_no_balance_is_found(self):
        def get_account_balance_account_bank(
                account_id):
            return []

        self.use_case = GetBalanceUseCase(
            get_account_balance_account_bank
        )

        self.assertEqual(self.use_case.get_account_balance(
            "123"), BankBalance(0, "USD"))


if __name__ == '__main__':
    unittest.main()
