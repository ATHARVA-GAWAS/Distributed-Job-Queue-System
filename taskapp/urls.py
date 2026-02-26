from django.urls import path
from .views import submit_task, task_status


urlpatterns = [
    path("submit/", submit_task),
    path("status/<uuid:task_id>/", task_status),
]