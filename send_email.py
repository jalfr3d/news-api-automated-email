import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(text_subject, email_body,receiver):
    sender = "EMAIL_SENDER"
    password = os.environ["PY_NEWS"]

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = text_subject

    body = email_body

    mimetext = MIMEText(body, 'html')
    message.attach(mimetext)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    message_text = message.as_string()
    server.sendmail(sender, receiver, message_text)
    print('Email sent!')
    server.quit()
