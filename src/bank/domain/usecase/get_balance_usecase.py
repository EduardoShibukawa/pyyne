from collections.abc import Callable
from functools import reduce

from src.bank.domain.balanceable import Balanceable
from src.bank.domain.bank_balance import BankBalance


class GetBalanceUseCase:

    def __init__(self,
                 get_account_balance_supplier: Callable[[
                     int], list[Balanceable]]
                 ):
        self.get_account_balance_supplier = get_account_balance_supplier

    def get_account_balance(self, account_id: int) -> list[Balanceable]:
        balances = self.get_account_balance_supplier(
            account_id)

        if not bool(balances):
            return BankBalance(0.0, "USD")

        def sum_balances(current: Balanceable, next: Balanceable):
            # We can assume all balances have the same currency
            return BankBalance(current.balance() + next.balance(), current.currency())

        return reduce(sum_balances, balances)
