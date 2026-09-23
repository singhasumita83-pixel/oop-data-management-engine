import csv
import json
from .accounts import SavingsAccount, CurrentAccount
from .ledger import Ledger


def save_json(ledger, filename):
    data = []
    for account in ledger.all_accounts():
        item = {
            "account_no": account.account_no,
            "owner": account.owner,
            "account_type": account.account_type(),
            "balance": account.balance,
        }
        if isinstance(account, SavingsAccount):
            item["interest_rate"] = account.interest_rate
        if isinstance(account, CurrentAccount):
            item["overdraft_limit"] = account.overdraft_limit
        data.append(item)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(filename):
    ledger = Ledger()
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        if item["account_type"] == "Savings":
            account = SavingsAccount(
                item["account_no"], item["owner"], item["balance"],
                item.get("interest_rate", 0.04)
            )
        elif item["account_type"] == "Current":
            account = CurrentAccount(
                item["account_no"], item["owner"], item["balance"],
                item.get("overdraft_limit", 1000.0)
            )
        else:
            account = Account(
                item["account_no"], item["owner"], item["balance"]
            )
        ledger.add_account(account)
    return ledger


def save_csv(ledger, filename):
    fields = [
        "account_no", "owner", "account_type", "balance",
        "interest_rate", "overdraft_limit"
    ]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for account in ledger.all_accounts():
            row = {
                "account_no": account.account_no,
                "owner": account.owner,
                "account_type": account.account_type(),
                "balance": account.balance,
                "interest_rate": getattr(account, "interest_rate", ""),
                "overdraft_limit": getattr(account, "overdraft_limit", ""),
            }
            writer.writerow(row)
