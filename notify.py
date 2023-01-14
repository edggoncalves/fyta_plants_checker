#!/usr/bin/env python3

import config
import pickle
from pathlib import Path
import os
from email.mime.text import MIMEText
# Gmail API utils
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import googleapiclient.discovery
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode

URL = ['https://mail.google.com/']
TOKEN = 'token.pickle'
CREDS_JSON = 'credentials.json'


def authenticate() -> googleapiclient.discovery.Resource:
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    creds_json = os.path.join(Path(__file__).parent.resolve(), CREDS_JSON)
    pickle_file = os.path.join(Path(__file__).parent.resolve(), TOKEN)
    if Path.is_file(Path(pickle_file)):
        with open(pickle_file, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_json, URL)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open(pickle_file, 'wb') as token:
            pickle.dump(creds, token)

    return googleapiclient.discovery.build('gmail', 'v1', credentials=creds)


def send_mail(destination, obj, body):
    conf = config.load_conf()
    service = authenticate()

    message = MIMEText(body)
    message['to'] = destination
    message['from'] = conf['email_config']['email']
    message['subject'] = obj

    enc_message = {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

    return service.users().messages().send(
        userId='me',
        body=enc_message
    ).execute()
