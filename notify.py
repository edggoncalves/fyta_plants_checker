import config
import smtplib
from configparser import ConfigParser
from email.message import EmailMessage

URL = 'smtp.gmail.com'
PORT = 587


def start_session(conf: ConfigParser) -> smtplib.SMTP:
    session = smtplib.SMTP(URL, PORT)
    session.starttls()
    user = conf['email_config']['email']
    password = conf['email_config']['password']
    session.login(user, password)

    return session


def send_mail(body: str) -> dict:
    conf = config.load_conf()
    session = start_session(conf)

    # Generate email
    msg = EmailMessage()
    msg['Subject'] = 'Your plants need attention!'
    msg['To'] = conf['email_config']['to']
    msg['From'] = conf['email_config']['email']
    msg.set_content(body)

    return session.send_message(msg)
