FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY watch_containers.py .

CMD ["python3", "watch_containers.py"]
