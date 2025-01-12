FROM python:3.12.7-slim
LABEL authors="Гриша"
ENV PYTHONPATH="${PYTHONPATH}:/app/backend"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ../../alembic.ini .

COPY ../../requirements.txt .

COPY ../../.env .

RUN pip install --no-cache -r requirements.txt

COPY ../../backend .