from celery import Celery


BACKEND_URL = 'redis://localhost:6379/1'
redis_url = 'redis://localhost:6379/0'
app = Celery('tasks' , broker=redis_url , backend=BACKEND_URL)


@app.task
def add(x,y):
    return x+y

