
FROM python:3.12-slim

WORKDIR /app

COPY app.py .

ENV MESSAGE="Hello from my Docker image!"

EXPOSE 8000

CMD ["python", "app.py"]
