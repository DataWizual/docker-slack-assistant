import docker
import time
import requests
import threading

print("🚀 Assistant started", flush=True)

WEBHOOK_URL = "https://hooks.slack.com/services/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"
client = docker.from_env()

def send_message(text: str):
    """Отправка сообщения в Slack"""
    try:
        r = requests.post(WEBHOOK_URL, json={"text": text}, timeout=5)
        if r.status_code == 200:
            print(f"✅ Sent to Slack: {text}")
        else:
            print(f"⚠️ Slack returned {r.status_code}: {r.text}")
    except Exception as e:
        print(f"❌ Slack error: {e}")

def monitor_logs(container):
    """Следим за логами контейнера"""
    print(f"👀 Start log monitoring for {container.name}")
    try:
        logs = container.logs(stream=True, tail=0, follow=True)
        for line in logs:
            line = line.decode("utf-8").strip()
            if line:
                print(f"[{container.name}] {line}")  # всегда печатаем
            if any(word in line for word in ["ERROR", "Traceback", "500"]):
                send_message(f"🚨 {container.name}: {line}")
    except Exception as e:
        print(f"❌ Log monitor error for {container.name}: {e}")

if __name__ == "__main__":
    print("🔍 Log monitor started...")
    monitored = set()

    while True:
        try:
            containers = client.containers.list()
            for c in containers:
                if c.id not in monitored:
                    monitored.add(c.id)
                    t = threading.Thread(target=monitor_logs, args=(c,))
                    t.daemon = True
                    t.start()
                    print(f"✅ Started monitoring {c.name}")
        except Exception as e:
            print(f"❌ Error in main loop: {e}")
        time.sleep(5)

