from pprint import pprint
import unittest
from src.bank.domain.usecase.print_balance_usecase import PrintBalanceUseCase
from src.integration.bank2.bank2_account_balance import Bank2AccountBalance
from src.bank.domain.bank_balance import BankBalance


class PrintBalanceUseCaseTest(unittest.TestCase):

    def test_should_sum_balance_when_currency_is_the_same(self):
        def get_account_balance_account_bank(
                account_id):
            return [
                BankBalance(100, "USD"),
                BankBalance(200, "USD")
            ]

        self.use_case = PrintBalanceUseCase(
            get_account_balance_account_bank
        )

        self.assertEqual(self.use_case.get_account_balance(
            "123"), [BankBalance(300, "USD")])

    def test_should_group_by_currency(self):
        def get_account_balance_account_bank(
                account_id):
            return [
                BankBalance(100, "USD"),
                BankBalance(200, "RS")
            ]

        self.use_case = PrintBalanceUseCase(
            get_account_balance_account_bank
        )

        self.assertEqual(self.use_case.get_account_balance(
            "123"), [BankBalance(100, "USD"), BankBalance(200, "RS")])


if __name__ == '__main__':
    unittest.main()
