import os
import json
from pathlib import Path

ACCOUNTS_FILE = Path(__file__).parent / "accounts.json"

def load_accounts():
    if not ACCOUNTS_FILE.exists():
        print("[!] accounts.json bulunamadı!")
        return []
    with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
        try:
            accounts = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[!] accounts.json okunamadı: {e}")
            return []

    result = []
    for acc in accounts:
        t = acc["type"].upper()
        email    = os.getenv(f"{t}_EMAIL")
        password = os.getenv(f"{t}_PASSWORD")
        server   = os.getenv(f"{t}_SERVER")
        if not email or not password or not server:
            print(f"[!] {acc['name']} için .env bilgileri eksik, atlanıyor.")
            continue
        result.append({
            "name":     acc["name"],
            "type":     acc["type"],
            "email":    email,
            "password": password,
            "server":   server,
        })

    print(f"[+] {len(result)} hesap yüklendi.")
    return result