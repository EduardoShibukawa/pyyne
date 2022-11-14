import unittest
from unittest.mock import MagicMock
from datetime import datetime
from src.bank.bank_controller import BankController


class GetTransactionTest(unittest.TestCase):

    def setUp(self):
        self.get_transactions = MagicMock()
        self.bank_controller = BankController(
            MagicMock(), self.get_transactions)

    def test_should_call_get_balance_use_case_once(self):
        self.bank_controller.get_transcations(
            123, datetime.today().date(), datetime.today().date())
        self.get_transactions.assert_called_once_with(
            123, datetime.today().date(), datetime.today().date())


if __name__ == '__main__':
    unittest.main()
