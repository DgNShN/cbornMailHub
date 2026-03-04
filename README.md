# cbornMailHub 📬

Python mail fetcher for Gmail and Outlook via IMAP with local SQLite storage and spam cleaner.

## Features
- Gmail and Outlook support
- Fetches unread emails automatically
- Spam/ad mail detection and deletion (cleaner.py)
- SQLite database indexing

## Installation
pip install msal python-dotenv imapclient pyzmail36

## Usage
1. Create a `.env` file with your mail credentials
2. Add account types to `accounts.json`
3. Run `python main.py` to fetch mails
4. Run `python cleaner.py` to delete spam

## Notes
- Never push `.env` to GitHub
- Gmail requires an App Password
