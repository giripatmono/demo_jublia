import os
import pytz
from datetime import datetime
from celery import Celery
from data.models import engine, Event
from sqlalchemy.orm import sessionmaker
from send_mail import send_mail

Session = sessionmaker(bind=engine)

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
celery.conf.timezone = 'Asia/Singapore'

celery.conf.beat_schedule = {
    # Executes send_email every minutes.
    'send-email-every-minute': {
        'task': 'tasks.send_email',
        'schedule': 60,  # 60 seconds
    },
}


@celery.task(name='tasks.send_email')
def send_email():

    tz = pytz.timezone('Asia/Singapore')
    singapore_now = datetime.now(tz).strftime("%Y-%m-%d %H:%M")

    # get & send event emails
    result = ['processsing send_email at {}'.format(singapore_now)]
    try:
        session = Session()
        for event in session.query(Event).filter_by(send_date=datetime.strptime(singapore_now, "%Y-%m-%d %H:%M")).all():
            result.append('send_email for event:{} subject:{}'.format(event.event_id, event.email_subject))
            try:
                send_mail(event.email_subject, event.email_body)
            except Exception as e:
                result.append('{} - {}'.format(type(e), str(e)))
    except Exception as e:
        result.append('{} - {}'.format(type(e), str(e)))
    finally:
        session.close()

    return str(result)
