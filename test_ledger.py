import pytest
from banking_ledger.accounts import Account
from banking_ledger.ledger import Ledger
from banking_ledger.exceptions import DuplicateAccountError, AccountNotFoundError


def test_add_and_get_account():
    ledger = Ledger()
    account = Account("A1", "Test", 500)
    ledger.add_account(account)
    assert ledger.get_account("A1") is account


def test_duplicate_account():
    ledger = Ledger()
    ledger.add_account(Account("A1", "First"))
    with pytest.raises(DuplicateAccountError):
        ledger.add_account(Account("A1", "Second"))


def test_missing_account():
    ledger = Ledger()
    with pytest.raises(AccountNotFoundError):
        ledger.get_account("404")


def test_remove_account():
    ledger = Ledger()
    ledger.add_account(Account("A1", "Test"))
    ledger.remove_account("A1")
    with pytest.raises(AccountNotFoundError):
        ledger.get_account("A1")


def test_total_balance():
    ledger = Ledger()
    ledger.add_account(Account("A1", "One", 100))
    ledger.add_account(Account("A2", "Two", 250))
    assert ledger.total_balance() == 350
