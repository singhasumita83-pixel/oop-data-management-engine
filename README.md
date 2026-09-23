# Banking Ledger – OOP Data Management Engine

A beginner-friendly Python project created for the **Core Algorithms, OOP Structures & Robust Error Handling** task.

## Features
- Object-oriented account hierarchy
- Inheritance: `SavingsAccount` and `CurrentAccount` inherit from `Account`
- Encapsulation using protected attributes and properties
- Polymorphism through `account_type()` and `withdraw()`
- Custom exception classes
- JSON persistence
- CSV export
- Unit testing with pytest
- Test coverage target above 80%

## Project Structure

```text
oop_data_management_engine/
├── banking_ledger/
│   ├── __init__.py
│   ├── accounts.py
│   ├── exceptions.py
│   ├── ledger.py
│   └── storage.py
├── tests/
│   ├── test_accounts.py
│   ├── test_ledger.py
│   └── test_storage.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the project
```bash
python main.py
```

### 3. Run tests
```bash
pytest -q
```

### 4. Check coverage
```bash
pytest --cov=banking_ledger --cov-report=term-missing
```

The test suite is designed to provide more than 80% coverage of the main package.

## OOP Concepts Demonstrated

**Inheritance:** SavingsAccount and CurrentAccount extend Account.

**Encapsulation:** Account data is stored using protected attributes such as `_balance`, with controlled access through properties and methods.

**Polymorphism:** Different account types provide their own `account_type()` and withdrawal behavior.

**Custom Exceptions:** Invalid operations raise meaningful exceptions such as `InvalidAmountError` and `InsufficientFundsError`.

## Sample Output

```text
=== Banking Ledger ===
SB101 - Sumita - Savings - 5775.00
CA201 - Student Business - Current - -500.00
Total balance: 5275.0
Data saved to accounts.json and accounts.csv.
```

## Expected Proof

This repository contains modular Python classes, JSON/CSV persistence, custom exceptions, and pytest unit tests.
