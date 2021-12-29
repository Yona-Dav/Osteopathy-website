from celery import shared_task,Celery
from time import sleep
from django.core.mail import send_mail, EmailMessage
from appointment.models import Schedule
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from django.template.loader import render_to_string
from django.conf import settings
import django

app = Celery('osteopath')


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@app.task(name="reminder_appointment")
def reminder_appointment():
    schedules = Schedule.objects.filter(date=date.today() + relativedelta(days=1)).exclude(owner='yona')
    for schedule in schedules:
        mail_subject = 'Confirm Appointment'
        message = render_to_string('confirmation_email.html', {
                'user': schedule,
            })
        to_email = schedule.owner.email
        email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
        email.send()