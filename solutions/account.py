class Account:
    def __init__(self, number: str, owner: str, balance: int = 0):
        if balance < 0:
            raise ValueError("Начальный остаток не может быть отрицательным")
        self._number = number
        self._owner = owner
        self._balance = balance

    @property
    def number(self):
        return self._number

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount

    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"