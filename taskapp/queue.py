import redis
import json

# -----------------------------
# Redis Configuration
# -----------------------------
REDIS_HOST = "localhost"
REDIS_PORT = 6379
QUEUE_NAME = "task_queue"


# -----------------------------
# Redis Connection
# -----------------------------
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)


# -----------------------------
# Enqueue Task
# -----------------------------
def enqueue_task(task_type, payload):
    """
    Push task into Redis queue
    """

    task = {
        "task_type": task_type,
        "payload": payload
    }

    r.lpush(QUEUE_NAME, json.dumps(task))

    print(f"[QUEUE] Task added → {task_type}")


# -----------------------------
# Dequeue Task
# -----------------------------
def dequeue():
    """
    Pop task from Redis queue
    Worker consumes from here
    """

    task = r.rpop(QUEUE_NAME)

    if task:
        return json.loads(task)

    return None


# -----------------------------
# Queue Size (for monitoring)
# -----------------------------
def get_queue_size():
    return r.llen(QUEUE_NAME)