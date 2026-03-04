import os
from pathlib import Path
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Klasör yapısı
BASE_DIR          = Path(__file__).parent
DATA_DIR          = BASE_DIR / "data"
MAIL_DIR          = DATA_DIR / "mails"
DB_PATH           = DATA_DIR / "mail_index.db"

# IMAP ayarları
IMAP_FOLDER       = "INBOX"
FETCH_ONLY_UNSEEN = True

# Ortam değişkenlerini oku
OUTLOOK_EMAIL      = os.getenv("OUTLOOK_EMAIL")
OUTLOOK_CLIENT_ID  = os.getenv("OUTLOOK_CLIENT_ID")
OUTLOOK_TENANT_ID  = os.getenv("OUTLOOK_TENANT_ID")
OUTLOOK_REDIRECT_URI = os.getenv("OUTLOOK_REDIRECT_URI")
OUTLOOK_AUTHORITY  = os.getenv("OUTLOOK_AUTHORITY")
OUTLOOK_SCOPES     = os.getenv("OUTLOOK_SCOPES", "").split()


def validate_env():
    missing = []
    for var_name, var_value in {
        "OUTLOOK_EMAIL":        OUTLOOK_EMAIL,
        "OUTLOOK_CLIENT_ID":    OUTLOOK_CLIENT_ID,
        "OUTLOOK_TENANT_ID":    OUTLOOK_TENANT_ID,
        "OUTLOOK_REDIRECT_URI": OUTLOOK_REDIRECT_URI,
        "OUTLOOK_AUTHORITY":    OUTLOOK_AUTHORITY,
        "OUTLOOK_SCOPES":       OUTLOOK_SCOPES,
    }.items():
        if not var_value:
            missing.append(var_name)
    if missing:
        print(f"[!] Eksik ortam değişkenleri: {', '.join(missing)}")
        print("[!] Lütfen .env dosyanı kontrol et!")
        return False
    return True


if __name__ == "__main__":
    print("CBORN MailHub Configurator 🧩")
    if validate_env():
        print("[+] .env yapılandırması başarılı ✅")
    else:
        print("[!] Yapılandırma başarısız ❌")