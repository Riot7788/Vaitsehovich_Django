import os
from celery.schedules import crontab, timedelta
from celery import Celery, shared_task
# from celery import shared_task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# @@ -14,10 +14,13 @@
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
# app.autodiscover_tasks([
#     "config.tasks",
#     "booking_app.tasks"
# ])


from celery import shared_task

@shared_task
def debug_task(second: int):
    from time import sleep
    sleep(second)
    return f'we sleep {second}'

@shared_task
def another_task():
    return 'another task'

# app.conf.beat_schedule = {
#     # Executes every 1 minutes
#     'sleep some seconds': {
#         'task': 'config.celery.debug_task',
#         'schedule': crontab(minute="*/1"),
#         'args': (10,),
#     },
# }

app.conf.beat_schedule = {
    # Выполняется каждые 3 минуты и 40 секунд
    'sleep_task_3m_40s': {
        'task': 'config.celery.debug_task',
        'schedule': timedelta(minutes=3, seconds=40),
        'args': (10,),
    },
    # Выполняется только 3 раза с 19 по 21 час, каждый час
    'sleep_task_3_times_19_to_21': {
        'task': 'config.celery.another_task',
        'schedule': crontab(hour='19,20,21'),
        'args': (),
        'options': {'expires': 60*60}  # Задача активна только в течение 1 часа после запуска
    },
}