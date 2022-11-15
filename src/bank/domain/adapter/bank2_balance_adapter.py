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

    def __repr__(self):
        details = '{'
        details += f'"accountBalance": {self.__account_balance__},'
        details += f'"currency": "{self.__currency__}"'
        details += '}'

        return details

    def __hash__(self):
        return hash(self.__account_balance__, self.__currency__)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.__account_balance__ == other.__account_balance__ and
            self.__currency__ == other.__currency__
        )
