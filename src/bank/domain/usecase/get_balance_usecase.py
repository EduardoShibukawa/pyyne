from functools import reduce

from src.integration.bank2.bank2_account_source import Bank2AccountSource
from src.integration.bank1.bank1_account_source import Bank1AccountSource
from src.bank.domain.adapter.bank2_balance_adapter import Bank2BalanceAdapter
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter
from src.bank.domain.bank_balance import BankBalance
from src.bank.domain.balanceable import Balanceable


class GetBalanceUseCase:

    def __init__(self,
                 get_account_balance_supplier
                 ):
        self.get_account_balance_supplier = get_account_balance_supplier

    def get_account_balance(self, account_id) -> list[Balanceable]:
        balances = self.get_account_balance_supplier(
            account_id)

        # We can assume all balances have the same currency
        return reduce(lambda b1, b2: BankBalance(b1.balance() + b2.balance(), b1.currency()), balances)
