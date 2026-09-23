# Implementation Note

## Project Title
**Banking Ledger – Object-Oriented Data Management Engine**

## Objective
The project implements a small banking ledger to demonstrate object-oriented programming, robust error handling, data persistence, and unit testing in Python.

## Implementation
A base `Account` class was created and extended by `SavingsAccount` and `CurrentAccount`. Encapsulation is demonstrated by protected balance data and properties. Polymorphism is demonstrated through account-specific behavior.

Custom exceptions were added for invalid amounts, insufficient funds, duplicate accounts, and missing accounts.

The ledger stores account objects in memory and supports adding, finding, removing, and calculating total balances.

JSON persistence is implemented for complete data storage and restoration. CSV export is included for simple tabular data handling.

Pytest tests cover account operations, exceptions, inheritance/polymorphism, ledger operations, and file persistence. Coverage can be verified using `pytest --cov=banking_ledger`.

## Technologies
- Python 3
- OOP
- JSON
- CSV
- Pytest
- Pytest-Cov

## Conclusion
The completed project satisfies the requested implementation requirements and provides a modular GitHub-ready structure for demonstration.
