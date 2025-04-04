import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from services.speech import speak

class EmailService:
    def send_email(self, recipient, subject, message):
        sender_email = os.getenv("EMAIL_ADDRESS")
        sender_password = os.getenv("EMAIL_PASSWORD")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())
            server.quit()
            speak("Email sent successfully!")
        except Exception as e:
            speak(f"Failed to send email: {e}")
