from pprint import pprint
from datetime import datetime
from src.bank.bank_controller import BankController
from src.bank.client.bank_client import BankClient
from src.bank.domain.usecase.get_balance_usecase import GetBalanceUseCase
from src.bank.domain.usecase.get_transactions_usecase import GetTransactionsUseCase
from src.integration.bank2.bank2_account_source import Bank2AccountSource
from src.integration.bank1.bank1_account_source import Bank1AccountSource

if __name__ == "__main__":
    bank_client = BankClient()
    bank_controller = BankController(
        get_balance_use_case=GetBalanceUseCase(
            bank_client.get_account_balance),
        get_transactions_use_case=GetTransactionsUseCase(
            bank_client.get_transactions)
    )

    balances = bank_controller.get_balances(123)
    transactions = bank_controller.get_transcations(
        123, datetime.today().date(), datetime.today().date())

    print("Account Balance:")
    pprint(balances)
    print("Transactions:")
    pprint(transactions)

    bank1_account_source = Bank1AccountSource()
    pprint("-" * 10)
    print("Account Balance Bank 1:")
    pprint(bank1_account_source.get_account_balance(123))
    pprint(bank1_account_source.get_account_currency(123))
    print("Transactions Bank 1:")
    pprint(bank1_account_source.get_transactions(
        123, datetime.today(), datetime.today()))

    bank2_account_source = Bank2AccountSource()
    pprint("-" * 10)
    print("Account Balance Bank 2:")
    pprint(bank2_account_source.get_account_balance(123))
    print("Transactions Bank 2:")
    pprint(bank2_account_source.get_transactions(
        123, datetime.today(), datetime.today()))
