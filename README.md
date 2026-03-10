# 🚀 Distributed Job Queue System (Celery-Inspired)

A lightweight **asynchronous job processing system** built using **Django, Redis, and Python**.

This project demonstrates a **producer–consumer architecture** where a Django API enqueues tasks into Redis and independent worker processes consume and execute them asynchronously.

The purpose of this project is to understand how background job systems such as Celery work internally and how distributed workers process tasks at scale.

---

# 📌 Features

* Asynchronous background task processing
* Redis-backed message queue
* Producer–consumer architecture
* Dynamic task dispatcher
* Bulk task ingestion via API
* Horizontally scalable workers
* Modular task registry system
* Simulated email and notification services

---

# 🏗 System Architecture

```
Client/API Request
       │
       ▼
Django API (Producer)
       │
       ▼
Redis Queue (Message Broker)
       │
       ▼
Worker Processes (Consumers)
       │
       ▼
Task Dispatcher
   ├── Email Task
   └── Notification Task
```

### Workflow

1. Client sends a request to the API
2. API enqueues the task into Redis
3. Worker picks the task from the Redis queue
4. Dispatcher routes the task to the correct handler
5. Task executes asynchronously in the background

---

# 🧠 Key Concepts Implemented

* Producer–Consumer Pattern
* Background Task Processing
* Message Queue Architecture
* Redis as Message Broker
* Horizontal Worker Scaling
* Dynamic Task Routing

---

# ⚙️ Tech Stack

* Python
* Django
* Redis
* REST APIs

---

# 📂 Project Structure

```
project-root
│
├── taskapp
│   ├── tasks
│   │   ├── email_task.py
│   │   └── notification_task.py
│   │
│   ├── queue.py
│   ├── dispatcher.py
│   └── worker.py
│
├── api
│   └── views.py
│
└── manage.py
```

---

# 🔧 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/job-queue-system.git
cd job-queue-system
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Start Redis

Make sure Redis is installed and running.

```
redis-server
```

---

# ▶️ Running the System

### Start the Worker

```
python worker.py
```

The worker will continuously poll the Redis queue and execute tasks.

Example output:

```
[WORKER 5680] Picked Task:
{'task_type': 'email', 'payload': {'to': 'user@gmail.com', 'subject': 'Hello'}}

[EMAIL] Sending email to user@gmail.com
[EMAIL] Email sent successfully
```

---

# 📡 API Usage

### Send Email Task

Endpoint:

```
POST /enqueue
```

Request Body:

```
{
  "task_type": "email",
  "payload": {
    "to": "user1@gmail.com",
    "subject": "Hello"
  }
}
```

---

### Send Notification Task

Endpoint:

```
POST /enqueue
```

Request Body:

```
{
  "task_type": "notify",
  "payload": {
    "user": "Atharva",
    "message": "Bulk Notification"
  }
}
```

---

# 📦 Bulk Task Submission

You can enqueue multiple tasks in one request.

Example:

```
[
  {
    "task_type": "email",
    "payload": {
      "to": "user1@gmail.com",
      "subject": "Hello 1"
    }
  },
  {
    "task_type": "notify",
    "payload": {
      "user": "Atharva",
      "message": "Bulk Notification"
    }
  }
]
```

Workers will process these tasks asynchronously.

---

# 🚀 Scalability

The system supports horizontal scaling.

You can start multiple workers:

```
python worker.py
python worker.py
python worker.py
```

All workers will compete for tasks from the Redis queue.

---

# ⚠️ Current Limitations

This project focuses on core queue mechanics.

Missing production features:

* Task retry mechanism
* Dead letter queue
* Task status tracking
* Monitoring dashboard
* Redis clustering

---

# 🔮 Future Improvements

* Retry mechanism
* Dead-letter queue
* Task acknowledgement system
* Monitoring with Prometheus / Grafana
* Dockerized deployment
* Priority task queues

---

# 🎯 Learning Outcomes

This project helped explore:

* Distributed system fundamentals
* Message queue architecture
* Asynchronous processing
* Worker-based parallel execution
* Backend system design patterns

---

# 👨‍💻 Author

**Atharva Gawas**

Data Engineer at Deloitte

---

# ⭐ Inspiration

Inspired by how production systems like Celery, Sidekiq, and RabbitMQ handle asynchronous background job processing.
