from celery import Celery

app = Celery('tasks', broker='amqp://pablo:12345@localhost:5672/', 
             backend='db+sqlite:///results.sqlite')

import os

#os.environ['DJANGO_SETTINGS_MODULE'] = "djangocelery.settings"
app.config_from_object('celery_app.celeryconfig')

@app.task(ignore_result=False)
def add(x, y):
    return x + y