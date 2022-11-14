from src.integration.bank1.bank1_account_source import Bank1AccountSource
from src.integration.bank2.bank2_account_source import Bank2AccountSource
from src.bank.domain.adapter.bank1_balance_adapter import Bank1BalanceAdapter
from src.bank.domain.adapter.bank2_balance_adapter import Bank2BalanceAdapter
from src.bank.domain.adapter.bank1_transaction_adapter import Bank1TransactionAdapter
from src.bank.domain.adapter.bank2_transaction_adapter import Bank2TransactionAdapter


class BankClient:
    def __init__(self):
        self.bank1_account_source = Bank1AccountSource()
        self.bank2_account_source = Bank2AccountSource()

    def get_account_balance(self, account_id):
        return [
            Bank1BalanceAdapter(
                self.bank1_account_source.get_account_balance(account_id),
                self.bank1_account_source.get_account_currency(account_id)
            ),
            Bank2BalanceAdapter(
                self.bank2_account_source.get_account_balance(account_id))
        ]

    def get_transactions(self, account_id, from_date, to_date):
        return [
            [Bank1TransactionAdapter(t) for t in self.bank1_account_source.get_transactions(
                account_id, from_date, to_date)],
            [Bank2TransactionAdapter(t) for t in self.bank2_account_source.get_transactions(
                account_id, from_date, to_date)]
        ]
