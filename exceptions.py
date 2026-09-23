class LedgerError(Exception):
    """Base exception for the banking ledger."""


class InvalidAmountError(LedgerError):
    """Raised when an amount is zero or negative."""


class InsufficientFundsError(LedgerError):
    """Raised when an account cannot cover a withdrawal."""


class DuplicateAccountError(LedgerError):
    """Raised when an account number already exists."""


class AccountNotFoundError(LedgerError):
    """Raised when an account cannot be found."""
