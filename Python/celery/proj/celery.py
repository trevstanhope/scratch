#!/usr/bin/python
# Celery Worker server for proj
# Started with: celery worker --app=proj -l info
from __future__ import absolute_import
from celery import Celery

# Primary configuration
celery = Celery('proj.celery', broker='amqp://', backend='amqp://', include=['proj.tasks'])

# Optional configuration, see the application user guide.
celery.conf.update(CELERY_TASK_RESULT_EXPIRES=3600)

# Main
if __name__ == '__main__':
  celery.start()
