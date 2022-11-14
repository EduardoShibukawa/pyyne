class Bank2AccountBalance:

    def __init__(self, balance, currency):
        self.balance = balance
        self.currency = currency

    def __repr__(self):
        details = '{'
        details += f'"accountBalance": {self.balance},'
        details += f'"currency": {self.currency}'
        details += '}'

        return details
