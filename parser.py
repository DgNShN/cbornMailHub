import pyzmail

def parse_raw_mail(raw_bytes):
    msg = pyzmail.PyzMessage.factory(raw_bytes)

    subject = msg.get_subject() or "no subject"

    sender = ""
    if msg.get_addresses("from"):
        sender = msg.get_addresses("from")[0][1]

    return {
        "subject": subject,
        "sender": sender
    }
