from collections.abc import Callable
from datetime import date

from src.bank.domain.transactionable import Transactionable


class GetTransactionsUseCase:

    def __init__(self,
                 get_transactions_supplier: Callable[[
                     int, date, date], list[Transactionable]]):
        self.get_transactions_supplier = get_transactions_supplier

    def get_transactions(self, account_id, from_date, to_date) -> list[Transactionable]:
        return self.get_transactions_supplier(account_id, from_date, to_date)
