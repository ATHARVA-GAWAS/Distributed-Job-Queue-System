import time


def send_notification(payload):
    user = payload.get("user")
    message = payload.get("message")

    print(f"[NOTIFY] Sending notification to {user}")

    time.sleep(2)

    print(f"[NOTIFY] Notification delivered: {message}")

    return "Notification Sent"
