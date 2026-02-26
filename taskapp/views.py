# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import create_task
from .models import Task
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