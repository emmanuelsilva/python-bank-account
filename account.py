from account_exception import InsufficientBalance

class Transaction:
    def __init__(self, type, amount, running_balance):
        self._type = type
        self._amount = amount
        self._running_balance = running_balance

    def type(self):
        return self._type

    def amount(self):
        return self._amount

    def running_balance(self):
        return self._running_balance

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