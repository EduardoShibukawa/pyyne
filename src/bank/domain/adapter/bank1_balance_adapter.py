from typing import Final


class Bank1BalanceAdapter:
    def __init__(self, acccount_balance: float, currency: str):
        self.__account_balance__: Final = acccount_balance
        self.__currency__: Final = currency

    def balance(self) -> float:
        return self.__account_balance__

    def currency(self) -> str:
        return self.__currency__
