FROM python:3.11-slim-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt