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