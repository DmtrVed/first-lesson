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


class SavingsAccount(Account):
    def __init__(self, number: str, owner: str, balance: int = 0, rate: float = 0.05):
        super().__init__(number, owner, balance)
        self._rate = rate

    @property
    def rate(self):
        return self._rate

    def add_interest(self):
        self._balance += self._balance * self._rate

    def __repr__(self):
        return f"SavingsAccount('{self.number}', '{self.owner}', {self.balance}, {self.rate})"


class CheckingAccount(Account):
    def __init__(self, number: str, owner: str, balance: int = 0, overdraft: int = 0):
        super().__init__(number, owner, balance)
        self._overdraft = overdraft

    @property
    def overdraft(self):
        return self._overdraft

    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if self._balance - amount < -self._overdraft:
            raise ValueError("Превышен лимит овердрафта")
        self._balance -= amount

    def __repr__(self):
        return f"CheckingAccount('{self.number}', '{self.owner}', {self.balance}, {self.overdraft})"