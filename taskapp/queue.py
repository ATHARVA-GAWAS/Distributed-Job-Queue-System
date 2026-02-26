import redis
from django.conf import settings

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)


def enqueue(task_id):
    redis_client.lpush(settings.QUEUE_NAME, str(task_id))


def dequeue():
    _, task_id = redis_client.brpop(settings.QUEUE_NAME)
    return task_id