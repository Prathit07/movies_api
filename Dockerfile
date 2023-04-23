FROM python:3.8-slim-buster

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -U pip setuptools wheel 

RUN pip install gunicorn uvloop httptools

RUN pip install -r /app/requirements.txt

COPY ./service/ /app

ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:80", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--chdir", "/app"]