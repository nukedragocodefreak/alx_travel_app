import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
