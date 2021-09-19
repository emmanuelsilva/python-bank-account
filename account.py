from transaction import Transaction
from account_exception import InsufficientBalance

class Account:

    def __init__(self, number):
        self.number = number
        self._balance = 0
        self.transactions = []

    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        self._add_transaction('DEPOSIT', amount)
        
    def withdraw(self, amount):
        self._check_balance(amount)
        self._balance -= amount
        self._add_transaction('WITHDRAW', amount)

    def _add_transaction(self, type, amount):
        self.transactions.append(Transaction(type, amount, running_balance=self._balance))

    def _check_balance(self, amount):
        if (self._balance < amount):
            msg = f"insufficient-balance=[account:{self.number}, balance:{self._balance}, amount:{amount}]"
            raise InsufficientBalance(msg)