import time
import os
import sys

# -----------------------------------
# Fix Import Path (VERY IMPORTANT)
# -----------------------------------
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(BASE_DIR)

# -----------------------------------
# Imports
# -----------------------------------
from taskapp.queue import dequeue
from taskapp.dispatcher import dispatch


# -----------------------------------
# Worker Info
# -----------------------------------
WORKER_ID = os.getpid()


def start_worker():
    print(f"\n🚀 Worker Started | ID: {WORKER_ID}\n")

    while True:

        task = dequeue()

        if task:
            print(f"\n[WORKER {WORKER_ID}] Picked Task:")
            print(task)

            try:
                result = dispatch(task)

                print(
                    f"[WORKER {WORKER_ID}] ✅ Completed → {result}"
                )

            except Exception as e:
                print(
                    f"[WORKER {WORKER_ID}] ❌ Failed → {e}"
                )

        else:
            time.sleep(1)


# -----------------------------------
# Entry Point
# -----------------------------------
if __name__ == "__main__":
    start_worker()