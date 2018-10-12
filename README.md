## Description

a simple web application that is able to serve a POST endpoint. The main
function of the endpoint is to store in the database an email for a particular group of recipients. The
emails are then to be sent ​ automatically​ at a later time


### Build & Launch

```bash
docker-compose up --build
```

This will expose the Flask application's endpoints on port `5000` as well as a flower server for monitoring workers on port `5555`

To shut down:

```bash
docker-compose down
```

### Endpoint to store email
- Method : `POST`
- Parameters :
  - event_id
  - email_subject
  - email_body
  - send_date (format "%Y-%m-%d %H:%M") (example:"15 Dec 2015 23:12")
- Request Example
```
curl -X POST localhost:5000/save_emails -d 'event_id=43' -d 'email_subject=Subject 43' -d 'email_body=Body 43' -d 'timestamp=2018-10-13 12:00'
```
- Response
```
{
    "message": "event is saved",
    "data": {
        "event_id": "21",
        "email_subject": "Subject 21",
        "email_body": "Body 21",
        "timestamp": "2018-10-11 12:21"
    }
}
```

### Monitor Task 
Celery is used for periodic task scheduling for sending email. The task is scheduled to be run for every minutes.
You can monitor the task run by accessing `http://localhost:5555/tasks`


---------

adapted from [https://github.com/mattkohl/docker-flask-celery-redis](https://github.com/mattkohl/docker-flask-celery-redis)