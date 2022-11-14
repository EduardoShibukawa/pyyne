from pprint import pprint
from datetime import datetime
from src.bank.bank_controller import BankController
from src.bank.client.bank_client import BankClient
from src.bank.domain.usecase.get_balance_usecase import GetBalanceUseCase
from src.bank.domain.usecase.get_transactions_usecase import GetTransactionsUseCase


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

    pprint(balances)
    pprint(transactions)
