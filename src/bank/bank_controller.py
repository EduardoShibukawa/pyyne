from src.bank.domain.usecase.get_balance_usecase import GetBalanceUseCase
from src.bank.domain.usecase.get_transactions_usecase import GetTransactionsUseCase
from src.bank.client.bank_client import BankClient


class BankController:

    def __init__(self, get_balance_use_case: GetBalanceUseCase, get_transactions_use_case: GetTransactionsUseCase):
        self.__get_balance_use_case__ = get_balance_use_case
        self.__get_transactions_use_case__ = get_transactions_use_case

    def get_balances(self, account_id):
        return self.__get_balance_use_case__.get_account_balance(account_id)

    def get_transcations(self, account_id, from_date, to_date):
        return self.__get_transactions_use_case__.get_transactions(account_id, from_date, to_date)
