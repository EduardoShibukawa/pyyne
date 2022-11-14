class Bank1Transaction:
    TYPE_CREDIT = 1
    TYPE_DEBIT = 2

    def __init__(self, amount, type, text):
        self.amount = amount
        self.type = type
        self.text = text

    def __repr__(self):
        details = '{'
        details += f'"amount"  : {self.amount},'
        details += f'"type": "{self.type}",'
        details += f'"text": "{self.text}"'
        details += '}'

        return details
