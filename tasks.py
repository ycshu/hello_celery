from celery import Celery
from local_settings import BROKER_URL, BACKEND_URL

# BROKER_URL = 'mongodb://localhost:27017/helloCeleryBroker'
# BACKEND_URL = 'mongodb://localhost:27017/helloCeleryBackend'

app = Celery('tasks', 
             broker=BROKER_URL,
             backend=BACKEND_URL)

app.conf.update(CELERY_SEND_TASK_SENT_EVENT = True)

@app.task
def add(x, y):
    return x + y

@app.task
def prod(x, y):
    return x*y

