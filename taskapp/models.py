from django.db import models
import uuid
# Create your models here.


class Task(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("PROCESSING", "PROCESSING"),
        ("SUCCESS", "SUCCESS"),
        ("FAILED", "FAILED"),
    ]

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)

    task_name = models.CharField(max_length=100)

    payload = models.JSONField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    retry_count = models.IntegerField(default=0)

    max_retries = models.ImageField(default=3)

    result = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
