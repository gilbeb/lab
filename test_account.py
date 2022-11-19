from pytest import *
from account import *

class Test:
    def test_init(self):
        self.test_account = Account('Hello')
        assert self.test_account.get_name() == 'Hello'
        assert self.test_account.get_balance() == 0


    def test_deposit(self):
        self.test_account = Account('John')
        assert self.test_account.deposit(6.2) == True
        assert self.test_account.get_balance() == approx(6.2, abs=0.001)
        assert self.test_account.deposit(0) == False
        assert self.test_account.get_balance() == approx(6.2, abs=0.001)
        assert self.test_account.deposit(-2) == False
        assert self.test_account.get_balance() == approx(6.2, abs=0.001)

    def test_withdraw(self):
        self.test_account = Account('With')
        assert self.test_account.deposit(6.2) == True
        assert self.test_account.withdraw(3) == True
        assert self.test_account.get_balance() == approx(3.2, abs=0.001)
        assert self.test_account.withdraw(6) == False
        assert self.test_account.get_balance() == approx(3.2, abs=0.001)
        assert self.test_account.withdraw(0) == False
        assert self.test_account.get_balance() == approx(3.2, abs=0.001)
        assert self.test_account.withdraw(-3) == False
        assert self.test_account.get_balance() == approx(3.2, abs=0.001)


