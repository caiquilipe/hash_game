FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

COPY src .

RUN pip install -r requirements.txt

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]