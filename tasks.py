from celery import Celery


BACKEND_BROKER = 'redis://localhost:6379/0'

app = Celery('tasks' , broker=BACKEND_BROKER)


@app.task
def reverse(string):
    return string[::-1]

