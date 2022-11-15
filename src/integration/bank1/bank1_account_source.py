from src.integration.bank1.bank1_transaction import Bank1Transaction


class Bank1AccountSource:
    def get_account_balance(self, account_id) -> float:
        return 215.5

    def get_account_currency(self, account_id) -> str:
        return "USD"

    def get_transactions(self, account_id, from_date, to_date) -> list[Bank1Transaction]:
        return [
            Bank1Transaction(
                100, Bank1Transaction.TYPE_CREDIT, "Check deposit"),
            Bank1Transaction(25.5, Bank1Transaction.TYPE_DEBIT,
                             "Debit card purchase"),
            Bank1Transaction(225, Bank1Transaction.TYPE_DEBIT, "Rent payment")
        ]
