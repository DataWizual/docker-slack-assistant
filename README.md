# 🚀 Docker Slack Assistant

Monitoring Docker containers and sending alerts to **Slack** whenever critical errors appear in logs.  
DevOps learning project by **Eldor Zufarov**.

---

## 📌 Features
- 🔍 Monitors logs from all containers defined in `docker-compose`.
- 🚨 Sends alerts to **Slack** when:
  - `ERROR` messages appear,
  - HTTP `500` responses occur,
  - or other critical events are detected.
- ⚡ Easy rebuild and deployment using **Docker Compose**.

---

## 🛠️ Tech Stack
- **Docker / Docker Compose**
- **Python 3.10 (slim)**
- **Slack Webhook API**
- **Nginx + Python backend**
- **WSL2 + Ubuntu 22.04 + VS Code**

---

## 📂 Project Structure
```
compose_test/
│── assistant/               # Log monitoring assistant
│   ├── Dockerfile
│   ├── requirements.txt
│   └── watch_containers.py
│
│── backend/                 # Python backend (HTTPServer)
│   └── app.py
│
│── nginx_conf/              # Nginx configuration
│   └── default.conf
│
│── docker-compose.yml       # Main compose file
│── .gitignore
│── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/<username>/docker-slack-assistant.git
cd docker-slack-assistant
```

### 2. Configure Slack Webhook
Create a `.env` file with:
```env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXX/YYY/ZZZ
```

### 3. Start the services
```bash
docker compose up -d --build
```

### 4. Test the backend
```bash
curl http://localhost:8083/app/
# Hello from Python in Docker Compose!
```

### 5. Generate an error
```bash
curl http://localhost:8083/app/error
```
👉 A 🚨 Slack notification will be sent.

---

## 📊 Example Slack Alert
```
:rotating_light: compose_test-web-1: "GET /app/error HTTP/1.1" 500
:rotating_light: compose_test-backend-1: ERROR: simulated failure
```

---

## 🎯 Project Goals
- Learn **Docker Compose** with real services.  
- Implement **log monitoring** in Python.  
- Integrate with **Slack** for alerts.  
- Prepare the foundation for next steps: **CI/CD, Kubernetes, Prometheus**.

---

## 📜 Changelog

### Day 1–2
- Set up Docker basics
- Ran first containers (`hello-world`, `alpine`)

### Day 3
- Added Nginx service in Docker
- Connected Nginx with a Python backend

### Day 4
- Created log monitoring assistant (Python + Docker SDK)
- Integrated Slack alerts for container events

### Day 5
- Added error simulation endpoint in backend (`/error`)
- Verified Slack integration with HTTP 500 responses

### Day 6
- Implemented log severity levels (INFO 🔵, WARNING ⚠️, ERROR 🚨)
- Added `.env` support for Slack webhook
- Fixed project structure (`backend/`, `nginx_conf/`)
- Updated `docker-compose.yml` with `depends_on`

---

## 🗺️ Roadmap

| Week | Focus Area                           | Progress ✅ |
|------|---------------------------------------|-------------|
| 1    | Linux basics, Docker fundamentals     | ✅ Completed |
| 2    | Docker deep dive, Nginx + Python app  | ✅ Completed |
| 3    | Docker Compose, monitoring assistant, Slack integration | ✅ Completed |
| 4    | Git & GitHub workflow, project structure fixes | ✅ Completed |
| 5    | CI/CD with GitHub Actions             | 🔄 In progress |
| 6    | Advanced monitoring (Prometheus, Grafana) | ⏳ Planned |
| 7    | Kubernetes basics                     | ⏳ Planned |
| 8    | Deployments on cloud (AWS/GCP/Azure)  | ⏳ Planned |

---

👨‍💻 Author: **Eldor Zufarov**  
📅 DevOps learning project (2025)
