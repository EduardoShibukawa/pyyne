import unittest
from src.bank.bank_controller import BankController


class PrinceBalanceTest(unittest.TestCase):
    def test_increment(self):
        bank_controller = BankController()
        self.assertEqual(bank_controller.print_balances(
        ), "Implement me to pull balance information from all available bank integrations and display them, one after the other.")


if __name__ == '__main__':
    unittest.main()
