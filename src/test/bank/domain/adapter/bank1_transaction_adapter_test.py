import unittest
from src.bank.domain.adapter.bank1_transaction_adapter import Bank1TransactionAdapter
from src.integration.bank1.bank1_transaction import Bank1Transaction
from src.bank.domain.transaction_type import TransactionType


class Bank1TransactionAdapterTest(unittest.TestCase):

    def setUp(self):
        self.bank1_transaction = Bank1Transaction(
            100, Bank1Transaction.TYPE_CREDIT, "Check deposit")
        self.bank1_transaction_adapter = Bank1TransactionAdapter(
            self.bank1_transaction)

    def test_should_have_same_text_as_bank1_transaction(self):
        self.assertEqual(self.bank1_transaction_adapter.text(),
                         self.bank1_transaction.text)

    def test_should_have_same_type_as_bank1_transaction(self):
        self.assertEqual(self.bank1_transaction_adapter.type(),
                         TransactionType.CREDIT)

    def test_should_have_same_amount_as_bank1_transaction(self):
        self.assertEqual(self.bank1_transaction_adapter.amount(),
                         self.bank1_transaction.amount)


if __name__ == '__main__':
    unittest.main()
