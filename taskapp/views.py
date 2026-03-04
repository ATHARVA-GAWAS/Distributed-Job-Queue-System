# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import create_task
from .models import Task

from django.http import JsonResponse
from taskapp.queue import enqueue_task


# Create your views here.


@api_view(["POST"])
def submit_task(request):

    task_name = request.data["task_name"]
    payload = request.data.get("payload", {})

    task = create_task(task_name, payload)

    return Response({
        "task_id": task.id,
        "status": task.status
    })


@api_view(["GET"])
def task_status(request, task_id):

    task = Task.objects.get(id=task_id)

    return Response({
        "status": task.status,
        "result": task.result
    })


@api_view(["POST"])
def send_email_view(request):

    enqueue_task(
        "send_email",
        {
            "to": "test@gmail.com",
            "subject": "Welcome!"
        }
    )

    return JsonResponse({"status": "Email queued"})


@api_view(["POST"])
def notify_view(request):

    enqueue_task(
        "send_notification",
        {
            "user": "Atharva",
            "message": "Job Completed!"
        }
    )

    return JsonResponse({"status": "Notification queued"})


@api_view(["POST"])
def bulk_tasks_view(request):
    tasks = request.data.get("tasks", [])

    if not tasks:
        return Response({"error": "No tasks provided"}, status=400)

    queued = []

    for task in tasks:
        task_type = task.get("type")

        if task_type not in ["email", "notify"]:
            continue

        enqueue_task(task_type, task)
        queued.append(task)

    return Response({
        "status": "Bulk tasks queued",
        "total_received": len(tasks),
        "total_queued": len(queued)
    })