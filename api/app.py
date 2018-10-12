import json
from flask import Flask
from flask import request
from datetime import datetime
from data.models import engine, Event
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/save_emails", methods=['POST'])
def save_emails():
    # get form data
    # print(request.form)
    event_id = request.form['event_id']
    email_subject = request.form['email_subject']
    email_body = request.form['email_body']
    send_date = datetime.strptime(request.form['timestamp'], "%Y-%m-%d %H:%M")

    # insert to database
    session = Session()
    event = Event(event_id=event_id, email_subject=email_subject, email_body=email_body, send_date=send_date)
    try:
        print('saving event..')
        session.add(event)
        session.commit()
    except Exception as e:
        print('{} - {}'.format(type(e), str(e)))
        session.rollback()
    finally:
        session.close()

    return json.dumps({
        'message': 'event is saved',
        'data': request.form
    })

