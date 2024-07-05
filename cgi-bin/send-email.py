#!/usr/bin/env python3

import cgi
import cgitb
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

cgitb.enable()  # Enable debugging

def main():
    print("Content-Type: application/json")
    print()  # End of headers

    form = cgi.FieldStorage()
    sender_email = form.getvalue('sender_email')
    receiver_email = form.getvalue('receiver_email')
    password = form.getvalue('password')
    subject = form.getvalue('subject')
    body = form.getvalue('body')

    if not (sender_email and receiver_email and password and subject and body):
        response = {"error": "All fields are required"}
        print(json.dumps(response))
        return

    try:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.send_message(message)

        response = {"success": "Email sent successfully!"}
    except Exception as e:
        response = {"error": str(e)}

    print(json.dumps(response))

if __name__ == "__main__":
    main()
