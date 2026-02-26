from .models import Task
from .queue import enqueue


def create_task(task_name, payload):

    task = Task.objects.create(
        task_name=task_name,
        payload=payload
    )

    enqueue(task.id)

    return task