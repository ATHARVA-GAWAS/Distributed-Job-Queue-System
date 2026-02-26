import os
import sys
import django
import time

# ✅ Add project root to Python path
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

# ✅ Load Django settings
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "mini_celery.settings"
)

django.setup()

# NOW Django apps are available
from taskapp.queue import dequeue, enqueue
from taskapp.models import Task
from taskapp.tasks import TASK_REGISTRY


print("✅ Worker started...")

while True:

    task_id = dequeue()

    task = Task.objects.get(id=task_id)

    task.status = "PROCESSING"
    task.save()

    try:
        func = TASK_REGISTRY[task.task_name]

        result = func(task.payload)

        task.status = "SUCCESS"
        task.result = result

    except Exception as e:

        task.retry_count += 1

        if task.retry_count < task.max_retries:
            enqueue(task.id)
            task.status = "PENDING"
        else:
            task.status = "FAILED"
            task.result = str(e)

    task.save()

    time.sleep(1)