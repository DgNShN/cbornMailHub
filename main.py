from config import MAIL_DIR
from database import init_db
from accounts import load_accounts
from fetcher import fetch_account

def main():
    print("[*] CBORN Mail Hub starting...")

    MAIL_DIR.mkdir(parents=True, exist_ok=True)
    init_db()

    accounts = load_accounts()

    for acc in accounts:
        fetch_account(acc)

    print("[✓] Fetch completed")

if __name__ == "__main__":
    main()
