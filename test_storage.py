from banking_ledger.accounts import SavingsAccount, CurrentAccount
from banking_ledger.ledger import Ledger
from banking_ledger.storage import save_json, load_json, save_csv


def create_ledger():
    ledger = Ledger()
    ledger.add_account(SavingsAccount("S1", "Alice", 1000, 0.05))
    ledger.add_account(CurrentAccount("C1", "Bob", 2000, 500))
    return ledger


def test_json_round_trip(tmp_path):
    original = create_ledger()
    file = tmp_path / "accounts.json"
    save_json(original, file)
    loaded = load_json(file)

    assert loaded.get_account("S1").balance == 1000
    assert loaded.get_account("S1").interest_rate == 0.05
    assert loaded.get_account("C1").overdraft_limit == 500


def test_csv_creation(tmp_path):
    ledger = create_ledger()
    file = tmp_path / "accounts.csv"
    save_csv(ledger, file)

    content = file.read_text(encoding="utf-8")
    assert "account_no" in content
    assert "S1" in content
    assert "C1" in content
