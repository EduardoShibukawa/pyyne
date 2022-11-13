from typing import Final
from src.integration.bank2.bank2_account_balance import Bank2AccountBalance


class Bank2BalanceAdapter:
    def __init__(self, bank2_account_balance: Bank2AccountBalance):
        self.__account_balance__: Final = bank2_account_balance.balance
        self.__currency__: Final = bank2_account_balance.currency

    def balance(self) -> float:
        return self.__account_balance__

    def currency(self) -> str:
        return self.__currency__
