import unittest
from src.bank.domain.adapter.bank2_transaction_adapter import Bank2TransactionAdapter
from src.integration.bank2.bank2_account_transaction import Bank2AccountTransaction
from src.bank.domain.transaction_type import TransactionType


class Bank2TransactionAdapterTest(unittest.TestCase):

    def setUp(self):
        self.bank2_transaction = Bank2AccountTransaction(
            125.0, Bank2AccountTransaction.TransactionType.DEBIT, "Amazon.com")
        self.bank2_transaction_adapter = Bank2TransactionAdapter(
            self.bank2_transaction)

    def test_should_have_same_text_as_bank1_transaction(self):
        self.assertEqual(self.bank2_transaction_adapter.text(),
                         self.bank2_transaction.text)

    def test_should_have_same_type_as_bank1_transaction(self):
        self.assertEqual(self.bank2_transaction_adapter.type(),
                         TransactionType.DEBIT)

    def test_should_have_same_amount_as_bank1_transaction(self):
        self.assertEqual(self.bank2_transaction_adapter.amount(),
                         self.bank2_transaction.amount)


if __name__ == '__main__':
    unittest.main()
