from .accounts import Account
from .exceptions import DuplicateAccountError, AccountNotFoundError


class Ledger:
    """Manages multiple account objects."""

    def __init__(self):
        self._accounts = {}

    def add_account(self, account):
        if account.account_no in self._accounts:
            raise DuplicateAccountError(
                f"Account {account.account_no} already exists."
            )
        self._accounts[account.account_no] = account

    def get_account(self, account_no):
        try:
            return self._accounts[str(account_no)]
        except KeyError:
            raise AccountNotFoundError(f"Account {account_no} not found.")

    def remove_account(self, account_no):
        self.get_account(account_no)
        del self._accounts[str(account_no)]

    def all_accounts(self):
        return list(self._accounts.values())

    def total_balance(self):
        return round(sum(account.balance for account in self._accounts.values()), 2)
