FROM python:3.8-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install nano -y
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
