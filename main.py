from banking_ledger.accounts import SavingsAccount, CurrentAccount
from banking_ledger.ledger import Ledger
from banking_ledger.storage import save_json, save_csv
from banking_ledger.exceptions import LedgerError


def main():
    ledger = Ledger()

    try:
        ledger.add_account(SavingsAccount("SB101", "Sumita", 5000, 0.05))
        ledger.add_account(CurrentAccount("CA201", "Student Business", 3000, 1000))

        ledger.get_account("SB101").deposit(1000)
        ledger.get_account("SB101").withdraw(500)
        ledger.get_account("SB101").add_interest()

        ledger.get_account("CA201").withdraw(3500)

        print("=== Banking Ledger ===")
        for account in ledger.all_accounts():
            print(account)
        print("Total balance:", ledger.total_balance())

        save_json(ledger, "accounts.json")
        save_csv(ledger, "accounts.csv")
        print("Data saved to accounts.json and accounts.csv.")

    except LedgerError as error:
        print("Ledger error:", error)


if __name__ == "__main__":
    main()
