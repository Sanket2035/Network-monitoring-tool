import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender_email, sender_password, recipient_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

# Example usage (replace with your actual email credentials)
# send_email("Test Subject", "This is a test email.", "your_email@gmail.com", "your_password", "recipient_email@example.com")