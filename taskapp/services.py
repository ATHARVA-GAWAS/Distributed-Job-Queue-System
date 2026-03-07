from .models import Task
from .queue import enqueue_task


def create_task(task_name, payload):

    task = Task.objects.create(
        task_name=task_name,
        payload=payload
    )

    enqueue_task(task.id)

    return task