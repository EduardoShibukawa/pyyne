from itertools import groupby
from operator import itemgetter

from src.integration.bank2.bank2_account_source import Bank2AccountSource
from src.integration.bank1.bank1_account_source import Bank1AccountSource
from src.bank.domain.adapter.bank2_balance_adapter import Bank2BalanceAdapter
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter
from src.bank.domain.transactionable import Transactionable


class GetTransactionsUseCase:

    def __init__(self,
                 get_transactions_supplier):
        self.get_transactions_supplier = get_transactions_supplier

    def get_transactions(self, account_id, from_date, to_date) -> list[Transactionable]:
        return self.get_transactions_supplier(account_id, from_date, to_date)
