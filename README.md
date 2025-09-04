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

👨‍💻 Author: **Eldor Zufarov**  
📅 DevOps learning project (2025)
