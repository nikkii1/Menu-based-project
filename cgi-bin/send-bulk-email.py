#!/usr/bin/env python
import cgi
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # Change according to your SMTP server configuration
SMTP_USERNAME = 'nikitanikki.gupta12@gmail.com'
SMTP_PASSWORD = 'vart lpco ciil bdnl'

# Function to send emails to multiple recipients
def send_bulk_emails(recipients, subject, message):
    try:
        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        for recipient_email in recipients:
            # Create message container (Multipart/Alternative)
            msg = MIMEMultipart('alternative')
            msg['From'] = SMTP_USERNAME
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach plain text message
            msg.attach(MIMEText(message, 'plain'))

            # Send email
            server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())

        # Disconnect from SMTP server
        server.quit()

        return True

    except Exception as e:
        print(f"Content-type: text/html\r\n\r\n")
        print(f"Failed to send email. Error: {str(e)}")
        return False

# Main CGI logic
def main():
    form = cgi.FieldStorage()

    recipients = form.getlist('recipients')
    subject = form.getvalue('subject')
    message = form.getvalue('message')

    success = send_bulk_emails(recipients, subject, message)

    if success:
        print(f"Content-type: text/html\r\n\r\n")
        print("Emails sent successfully!")
    else:
        print(f"Content-type: text/html\r\n\r\n")
        print("Failed to send emails.")

if __name__ == '__main__':
    main()
