import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cp_aggregator.settings')

app = Celery('cp_aggregator')
app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
