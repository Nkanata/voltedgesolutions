import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTING_MODULE', 'voltEdgeSolutions.setting')

app = Celery('voltEdgeSolutions', broker='pyamqp://guest@localhost//')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
