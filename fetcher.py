from imapclient import IMAPClient
from datetime import datetime
from pathlib import Path

from config import MAIL_DIR, IMAP_FOLDER, FETCH_ONLY_UNSEEN
from parser import parse_raw_mail
from database import insert_mail

def fetch_account(account):
    print(f"[+] Connecting: {account['name']}")

    with IMAPClient(account["server"], ssl=True) as server:
        server.login(account["email"], account["password"])
        server.select_folder(IMAP_FOLDER)

        search_criteria = ["UNSEEN"] if FETCH_ONLY_UNSEEN else ["ALL"]
        messages = server.search(search_criteria)

        print(f"    {len(messages)} mail bulundu")

        total = len(messages)
        for i, uid in enumerate(messages, 1):
            raw = server.fetch([uid], ["RFC822"])[uid][b"RFC822"]

            parsed = parse_raw_mail(raw)

            now = datetime.now()
            folder = MAIL_DIR / now.strftime("%Y/%m")
            folder.mkdir(parents=True, exist_ok=True)

            filename = f"{now.strftime('%H%M%S')}_{account['name']}.eml"
            file_path = folder / filename

            with open(file_path, "wb") as f:
                f.write(raw)

            insert_mail(
                account=account["name"],
                sender=parsed["sender"],
                subject=parsed["subject"],
                date=now.isoformat(),
                file_path=str(file_path)
            )

            server.add_flags(uid, ["\\Seen"])
            print(f"    [{i}/{total}] {parsed['subject'][:50]}")