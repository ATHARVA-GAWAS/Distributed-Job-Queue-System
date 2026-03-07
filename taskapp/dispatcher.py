from taskapp.tasks.email_task import send_email
from taskapp.tasks.notification_task import send_notification


TASK_REGISTRY = {
    "email": send_email,
    "notify": send_notification,
}


def dispatch(task):
    task_type = task.get("task_type")
    payload = task.get("payload")

    if task_type not in TASK_REGISTRY:
        print("❌ Unknown task type")
        return None

    func = TASK_REGISTRY[task_type]

    result = func(payload)

    return result