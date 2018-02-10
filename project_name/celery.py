from __future__ import absolute_import, unicode_literals

import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')

app = Celery('{{ project_name }}')


class Config:
    broker_url = 'amqp://{username}:{password}@{host}:{port}'.format(
        username=os.environ['BROKER_USERNAME'],
        password=os.environ['BROKER_PASSWORD'],
        host=os.environ['BROKER_HOST'],
        port=os.environ['BROKER_PORT']
    )


app.config_from_object(Config)

app.autodiscover_tasks()
