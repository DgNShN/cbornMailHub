import os
import sqlite3
from config import DB_PATH

# Silinecek anahtar kelimeler (konu veya göndericide geçenler)
KEYWORDS = [
    "sale", "offer", "discount", "aliexpress", "alibaba",
    "promo", "deal", "% off", "unsubscribe", "newsletter"
]

def delete_spam(dry_run=True):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT id, sender, subject, file_path FROM mails")
    all_mails = cur.fetchall()

    to_delete = []
    for mail_id, sender, subject, file_path in all_mails:
        text = f"{sender} {subject}".lower()
        if any(kw.lower() in text for kw in KEYWORDS):
            to_delete.append((mail_id, sender, subject, file_path))

    print(f"[*] {len(to_delete)} reklam maili bulundu:\n")
    for mail_id, sender, subject, file_path in to_delete:
        print(f"  [{mail_id}] {sender} | {subject[:60]}")

    if dry_run:
        print("\n[!] DRY RUN — hiçbir şey silinmedi. Silmek için dry_run=False yap.")
        conn.close()
        return

    for mail_id, sender, subject, file_path in to_delete:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
        cur.execute("DELETE FROM mails WHERE id = ?", (mail_id,))

    conn.commit()
    conn.close()
    print(f"\n[✓] {len(to_delete)} mail silindi.")

if __name__ == "__main__":
    delete_spam(dry_run=False)  # önce önizleme, silmek için False yap