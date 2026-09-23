import pytest
from banking_ledger.accounts import Account, SavingsAccount, CurrentAccount
from banking_ledger.exceptions import InvalidAmountError, InsufficientFundsError


def test_account_deposit_and_withdraw():
    account = Account("A1", "Test", 1000)
    account.deposit(500)
    account.withdraw(200)
    assert account.balance == 1300


def test_invalid_deposit():
    account = Account("A1", "Test")
    with pytest.raises(InvalidAmountError):
        account.deposit(0)


def test_invalid_withdrawal():
    account = Account("A1", "Test", 100)
    with pytest.raises(InvalidAmountError):
        account.withdraw(-5)


def test_insufficient_funds():
    account = Account("A1", "Test", 100)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(101)


def test_savings_interest():
    account = SavingsAccount("S1", "Saver", 1000, 0.10)
    account.add_interest()
    assert account.balance == 1100


def test_current_account_overdraft():
    account = CurrentAccount("C1", "Business", 100, 500)
    account.withdraw(500)
    assert account.balance == -400


def test_current_account_overdraft_limit():
    account = CurrentAccount("C1", "Business", 100, 500)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(601)


def test_polymorphism():
    accounts = [
        SavingsAccount("S1", "A", 100),
        CurrentAccount("C1", "B", 100)
    ]
    assert [a.account_type() for a in accounts] == ["Savings", "Current"]
