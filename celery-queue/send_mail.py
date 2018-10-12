import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# email server for sending
EMAIL_SERVER = os.environ.get('EMAIL_SERVER')
EMAIL_SERVER_PORT = os.environ.get('EMAIL_SERVER_PORT')
EMAIL_LOGIN = os.environ.get('EMAIL_LOGIN')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


def send_mail(email_subject, email_body):

    # set up the SMTP server
    s = smtplib.SMTP(host=EMAIL_SERVER, port=EMAIL_SERVER_PORT)
    s.starttls()
    s.login(EMAIL_LOGIN, EMAIL_PASSWORD)

    # For each recipient, send the email:
    for email in get_email_recipients():
        msg = MIMEMultipart()  # create a message

        message = email_body

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = EMAIL_LOGIN
        msg['To'] = email
        msg['Subject'] = email_subject

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


def get_email_recipients(filename):
    """
    Return email recipients
    """
    emails = []
    return emails
