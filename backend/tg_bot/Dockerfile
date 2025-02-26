FROM python:3.13.2-slim
LABEL authors="Гриша"
ENV PYTHONPATH="${PYTHONPATH}:/backend"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY . .
