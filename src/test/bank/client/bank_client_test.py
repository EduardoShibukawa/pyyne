import unittest
from datetime import datetime
from src.bank.client.bank_client import BankClient
from src.integration.bank1.bank1_account_source import Bank1AccountSource
from src.integration.bank2.bank2_account_source import Bank2AccountSource
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter
from src.bank.domain.adapter.bank2_balance_adapter import Bank2BalanceAdapter
from src.bank.domain.adapter.bank1_transaction_adapter import Bank1TransactionAdapter
from src.bank.domain.adapter.bank2_transaction_adapter import Bank2TransactionAdapter


class BankClientTest(unittest.TestCase):

    def setUp(self):
        self.client = BankClient()

    def test_should_return_correctly_account_balance(self):
        self.assertEquals(
            self.client.get_account_balance(123),
            [
                Bank1BalanceAdapter(
                    Bank1AccountSource().get_account_balance(123),
                    Bank1AccountSource().get_account_currency(123)
                ),
                Bank2BalanceAdapter(
                    Bank2AccountSource().get_account_balance(123))
            ]
        )

    def test_should_return_correctly_account_transaction(self):
        self.assertEquals(
            self.client.get_transactions(
                123, datetime.today(), datetime.today()),
            [
                [Bank1TransactionAdapter(t) for t in Bank1AccountSource().get_transactions(
                    123, datetime.today(), datetime.today())],
                [Bank2TransactionAdapter(t) for t in
                    Bank2AccountSource().get_transactions(123, datetime.today(), datetime.today())]
            ]
        )


if __name__ == '__main__':
    unittest.main()
