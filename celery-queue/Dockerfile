FROM python:2.7-alpine

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

# install requirements
RUN mkdir -p /queue
COPY ./celery-queue/requirements.txt /queue
WORKDIR /queue
RUN pip install -r requirements.txt

COPY ./celery-queue /queue
COPY ./data /queue/data

ENTRYPOINT celery -A tasks worker --loglevel=info