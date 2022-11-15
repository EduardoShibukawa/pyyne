import unittest
from datetime import datetime
from src.bank.domain.usecase.get_transactions_usecase import GetTransactionsUseCase
from src.bank.domain.transaction_type import TransactionType


class GetBalanceUseCaseTest(unittest.TestCase):
    class BankTransaction:

        def __init__(self, amount, type, text):
            self.__amount__ = amount
            self.__type__ = type
            self.__text__ = text

        def amount(self) -> float:
            return self.__amount__

        def type(self) -> TransactionType:
            return self.__type__

        def text(self) -> str:
            return self.__text__

        def __hash__(self):
            return hash(self.__amount__, self.__type__, self.__text__)

        def __eq__(self, other):
            return (
                self.__class__ == other.__class__ and
                self.__amount__ == other.__amount__ and
                self.__type__ == other.__type__ and
                self.__text__ == other.__text__
            )

        def __repr__(self):
            details = '{'
            details += f'"amount"  : {self.__amount__},'
            details += f'"type": "{self.__type__}",'
            details += f'"text": "{self.__text__}"'
            details += '}'

            return details

    def test_should_return_transactions(self):
        transactions = [
            GetBalanceUseCaseTest.BankTransaction(
                100, TransactionType.CREDIT, "Check deposit"),
            GetBalanceUseCaseTest.BankTransaction(
                25.5, TransactionType.DEBIT, "Debit card purchase"),
            GetBalanceUseCaseTest.BankTransaction(
                225, TransactionType.DEBIT, "Rent payment"),
            GetBalanceUseCaseTest.BankTransaction(
                125.0, TransactionType.DEBIT, "Amazon.com"),
            GetBalanceUseCaseTest.BankTransaction(
                500.0, TransactionType.DEBIT, "Car insurance"),
            GetBalanceUseCaseTest.BankTransaction(
                800.0, TransactionType.CREDIT, "Salary")
        ]

        def get_transactions(
                account_id, from_date, to_date):
            return transactions

        self.use_case = GetTransactionsUseCase(
            get_transactions
        )

        self.assertEqual(self.use_case.get_transactions(
            123, datetime.today(), datetime.today()), transactions)


if __name__ == '__main__':
    unittest.main()
