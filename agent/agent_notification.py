import smtplib
from email.mime.text import MIMEText
import requests

class NotificationAgent:
    def __init__(self, email_config=None, slack_webhook=None):
        self.email_config = email_config
        self.slack_webhook = slack_webhook

    def notify_console(self, message):
        print(f"[NOTIFY] {message}")

    def notify_email(self, subject, message):
        if not self.email_config:
            return
        
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.email_config["sender"]
        msg['To'] = self.email_config["receiver"]

        with smtplib.SMTP(self.email_config["smtp"], self.email_config["port"]) as server:
            server.starttls()
            server.login(self.email_config["sender"], self.email_config["password"])
            server.sendmail(self.email_config["sender"], self.email_config["receiver"], msg.as_string())

    def notify_slack(self, message):
        if not self.slack_webhook:
            return

        payload = {"text": message}
        try:
            requests.post(self.slack_webhook, json=payload)
        except:
            pass
