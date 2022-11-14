from typing import Final


class Bank1BalanceAdapter:
    def __init__(self, acccount_balance: float, currency: str):
        self.__account_balance__: Final = acccount_balance
        self.__currency__: Final = currency

    def balance(self) -> float:
        return self.__account_balance__

    def currency(self) -> str:
        return self.__currency__

    def __hash__(self):
        return hash(self.__account_balance__, self.__currency__)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.__account_balance__ == other.__account_balance__ and
            self.__currency__ == other.__currency__
        )

    def __repr__(self):
        details = '{'
        details += f'"accountBalance": {self.__account_balance__},'
        details += f'"currency": {self.__currency__}'
        details += '}'

        return details
