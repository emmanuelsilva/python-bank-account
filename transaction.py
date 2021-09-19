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