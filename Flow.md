Client Request
      ↓
Django API
      ↓
Create Task in DB
      ↓
Push Task ID → Redis Queue
      ↓
Worker pulls task
      ↓
Executes task
      ↓
Updates DB status



1) Django API (Producer):
Accepts HTTP requests and pushes tasks to Redis.

2) Redis (Broker):
Stores queued jobs.

3) Worker(s) (Consumers):
Continuously pull tasks from Redis and execute them.

4) Task Dispatcher:
Decides which function runs (email, notification, etc.)