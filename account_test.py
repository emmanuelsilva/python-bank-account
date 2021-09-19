from unittest import TestCase
from pytest import raises

from account import Account
from account_exception import InsufficientBalance

class AccountTest(TestCase):

    def test_should_change_balance_after_deposit(self):
        account = Account("123")
        account.deposit(100)

        assert account.balance() == 100

    def test_should_create_deposit_transaction(self):
        account = Account("123")
        account.deposit(100)

        transaction = account.transactions[0]
        assert transaction.type() == "DEPOSIT"
        assert transaction.amount() == 100
        assert transaction.running_balance() == 100

    def test_should_change_balance_after_withdraw(self):
        account = Account("123")
        account.deposit(100)
        account.withdraw(30)

        assert account.balance() == 70

    def test_should_create_withdraw_transaction(self):
        account = Account("123")
        account.deposit(100)
        account.withdraw(25)

        transaction = account.transactions[1]
        assert transaction.type() == "WITHDRAW"
        assert transaction.amount() == 25
        assert transaction.running_balance() == 75

    def test_should_withdraw_entire_balance(self):
        account = Account("123")
        account.deposit(100)
        account.withdraw(100)

        assert account.balance() == 0

    def test_should_fail_when_balance_is_insufficient(self):
        account = Account("123")
        account.deposit(50)

        with raises(InsufficientBalance):
            account.withdraw(100)

    def test_should_compute_running_balance_for_every_transaction(self):
        account = Account("123")
        account.deposit(100)
        account.withdraw(50)
        account.withdraw(50)
    
        assert account.transactions[0].running_balance() == 100
        assert account.transactions[1].running_balance() == 50
        assert account.transactions[2].running_balance() == 0

