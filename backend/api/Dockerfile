FROM python:3.12.7-slim
LABEL authors="Гриша"
ENV PYTHONPATH="${PYTHONPATH}:/app/backend"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY . .

RUN pip install --no-cache -r requirements.txt
