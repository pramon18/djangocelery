from celery import Celery

app = Celery('tasks', broker='amqp://pablo:123456@localhost:5672/celery', 
             backend='db+sqlite:///results.sqlite')

@app.task(ignore_result=False)
def add(x, y):
    return x + y