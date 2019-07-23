# Biwott
from celery import Celery

app = Celery('tasks', backend='rpc://', result_backend='rpc://', broker='pyamqp://guest@localhost//')


@app.task
def reverse(string):
    return string[:: -1]

