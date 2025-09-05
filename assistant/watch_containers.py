import os
import docker
import requests

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_message(message: str):
    if SLACK_WEBHOOK_URL:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message})
    else:
        print(f"⚠️ No Slack webhook configured: {message}", flush=True)

def classify_log(line: str) -> str | None:
    """Classify logs by severity and return formatted string"""
    if "ERROR" in line or "500" in line:
        return f"🚨 {line}"
    elif "WARNING" in line or "WARN" in line:
        return f"⚠️ {line}"
    elif "INFO" in line:
        return f"🔵 {line}"
    else:
        return None

def monitor_container(container):
    print(f"👀 Start log monitoring for {container.name}", flush=True)
    try:
        for raw_line in container.logs(stream=True, follow=True):
            try:
                line = raw_line.decode("utf-8", errors="ignore").strip()
            except Exception as e:
                print(f"⚠️ Log decode error for {container.name}: {e}", flush=True)
                continue

            classified = classify_log(line)
            if classified:
                msg = f"{container.name}: {classified}"
                send_slack_message(msg)
                print(f"✅ Sent to Slack: {msg}", flush=True)
    except Exception as e:
        print(f"❌ Log monitor error for {container.name}: {e}", flush=True)

if __name__ == "__main__":
    print("🚀 Assistant started", flush=True)
    client = docker.from_env()

    for container in client.containers.list():
        monitor_container(container)
