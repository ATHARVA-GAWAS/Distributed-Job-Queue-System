import time


def send_email(payload):
    to = payload.get("to")
    subject = payload.get("subject")

    print(f"[EMAIL] Sending email to {to}")

    time.sleep(3)

    print(f"[EMAIL] Email sent to {to} | Subject: {subject}")

    return "Email Sent"
