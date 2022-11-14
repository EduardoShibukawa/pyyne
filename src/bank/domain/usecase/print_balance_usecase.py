from itertools import groupby
from operator import itemgetter

from src.integration.bank2.bank2_account_source import Bank2AccountSource
from src.integration.bank1.bank1_account_source import Bank1AccountSource
from src.bank.domain.adapter.bank2_balance_adapter import Bank2BalanceAdapter
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter
from src.bank.domain.bank_balance import BankBalance


class PrintBalanceUseCase:

    def __init__(self,
                 get_account_balance_supplier
                 ):
        self.get_account_balance_supplier = get_account_balance_supplier

    def get_account_balance(self, account_id):
        bank1_account, bank2_account = self.get_account_balance_supplier(
            account_id)

        if (bank1_account.currency() == bank2_account.currency()):
            return [BankBalance(bank1_account.balance() + bank2_account.balance(), bank1_account.currency())]

        return [
            bank1_account,
            bank2_account
        ]
