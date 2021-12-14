from config import SENDGRID_API_KEY, TEST_EMAIL, TEST_SEND_TO_EMAIL
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class SendGrid():
    
    def __init__(self, sendgrid = SendGridAPIClient(SENDGRID_API_KEY)):
        self.sendgrid = sendgrid
        
    def post_email(self, subject, html_content,from_email=TEST_EMAIL, to_emails=TEST_SEND_TO_EMAIL):
        
        message = Mail(
            from_email=from_email,
            to_emails=to_emails,
            subject=subject,
            html_content=html_content
        )
        
        return message