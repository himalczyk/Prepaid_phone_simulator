from twilio.rest import Client
from config import TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, TWILIO_SID, TEST_NUMBER

class TwilioClient:
    
    def __init__(self, client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)):
        
        self.client = client

    def post_sms(self, message_body):
        
        message = self.client.messages.create(
                        body=message_body,
                        from_=TWILIO_PHONE_NUMBER,
                        to=TEST_NUMBER
                    )
        return message
        
    def post_mms(self, message_body, image_url):
        
        message = self.client.messages.create(
                        body=message_body,
                        from_=TWILIO_PHONE_NUMBER,
                        media_url = [image_url],
                        to=TEST_NUMBER
                    )
        
        return message
        
        