import unittest
from datetime import datetime
from unittest.mock import MagicMock

from src.bank.bank_controller import BankController
from src.bank.domain.usecase.get_transactions_usecase import \
    GetTransactionsUseCase


class GetTransactionTest(unittest.TestCase):

    def setUp(self):
        self.get_transactions = GetTransactionsUseCase(MagicMock())
        self.get_transactions.get_transactions = MagicMock()
        self.bank_controller = BankController(
            MagicMock(), self.get_transactions)

    def test_should_call_get_balance_use_case_once(self):
        self.bank_controller.get_transcations(
            123, datetime.today().date(), datetime.today().date())
        self.get_transactions.get_transactions.assert_called_once_with(
            123, datetime.today().date(), datetime.today().date())


if __name__ == '__main__':
    unittest.main()
