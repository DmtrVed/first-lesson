class Account:
    def __init__(self, number, owner, balance):
        if balance < 0:
            raise ValueError("нельзя")
        self.number = number
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
    def __repr__(self):
        return f"Account({self.number}, {self.owner}, {self.balance})"