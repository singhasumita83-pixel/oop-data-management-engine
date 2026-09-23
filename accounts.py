from .exceptions import InvalidAmountError, InsufficientFundsError


class Account:
    """Base bank account demonstrating encapsulation."""

    def __init__(self, account_no, owner, balance=0.0):
        self._account_no = str(account_no)
        self._owner = owner
        self._balance = float(balance)

    @property
    def account_no(self):
        return self._account_no

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return round(self._balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds.")
        self._balance -= amount

    def account_type(self):
        return "General"

    def __str__(self):
        return f"{self.account_no} - {self.owner} - {self.account_type()} - {self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_no, owner, balance=0.0, interest_rate=0.04):
        super().__init__(account_no, owner, balance)
        self.interest_rate = float(interest_rate)

    def account_type(self):
        return "Savings"

    def add_interest(self):
        self._balance += self._balance * self.interest_rate


class CurrentAccount(Account):
    def __init__(self, account_no, owner, balance=0.0, overdraft_limit=1000.0):
        super().__init__(account_no, owner, balance)
        self.overdraft_limit = float(overdraft_limit)

    def account_type(self):
        return "Current"

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self._balance + self.overdraft_limit:
            raise InsufficientFundsError("Overdraft limit exceeded.")
        self._balance -= amount
