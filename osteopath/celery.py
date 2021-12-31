from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osteopath.settings')

from django.conf import settings  # noqa

app = Celery('osteopath')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# CELERY_BEAT_SCHEDULE = {
#     'send-mail-every-day':{
#         'task':'reminder_appointment',
#         'schedule': crontab(minute='*/5')
#     }
# }

app.conf.beat_schedule = {
    'add-every-day': {
        'task':'reminder_appointment',
        'schedule': crontab(minute='*/5')
    }

}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))



