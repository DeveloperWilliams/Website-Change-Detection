# change_detection.py

import requests
from bs4 import BeautifulSoup
import smtplib

class ChangeDetector:
    def __init__(self, url, email_config):
        self.url = url
        self.email_config = email_config
        self.old_content = None

    def fetch_content(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()

    def check_for_changes(self):
        new_content = self.fetch_content()
        if self.old_content and self.old_content != new_content:
            self.send_email()
        self.old_content = new_content

    def send_email(self):
        with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
            server.login(self.email_config['username'], self.email_config['password'])
            message = "Subject: Website Change Detected\n\nChanges have been detected on the website."
            server.sendmail(self.email_config['from_email'], self.email_config['to_email'], message)
        print("Email sent.") # Print a message to the console

# Example usage
email_config = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'username': 'your_email@gmail.com',
    'password': 'your_password',
    'from_email': 'your_email@gmail.com',
    'to_email': 'recipient_email@gmail.com'
}
detector = ChangeDetector("http://example.com", email_config)
detector.check_for_changes() # Check for changes
