from django.urls import path
from .views import submit_task, task_status, send_email_view, notify_view, bulk_tasks_view


urlpatterns = [
    path("submit/", submit_task),
    path("status/<uuid:task_id>/", task_status),
    path("send-email/", send_email_view),
    path("notify/", notify_view),
    path("bulk/", bulk_tasks_view),
]