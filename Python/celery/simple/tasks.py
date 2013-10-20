from celery import Celery

celery = Celery('tasks', backend='amqp', broker='amqp://')

@celery.task
def add(x, y):
    return x + y
