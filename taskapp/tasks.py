import time

import random


def sleep_task(payload):
    duration = payload.get("duration", 5)

    print(f"Sleeping {duration}s")
    time.sleep(duration)

    if random.random() < 0.3:
        raise Exception("Random Failure")
    
    return f"Slept {duration} seconds"


TASK_REGISTRY = {
    "sleep_task": sleep_task
}