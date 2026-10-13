class Account:
    def __init__(self, number, owner, balance):
        if balance <= 0:
            raise ValueError("нельзя")
        self.number = number
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        else:
            self.balance -= amount
    def __repr__(self):
        return f"Account({self.number}, {self.owner}, {self.balance})"