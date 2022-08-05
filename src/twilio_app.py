"""Twilio API module used to send SMS, MMS and automated voice call messages."""


from twilio.rest import Client
from config import TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, TWILIO_SID, TEST_NUMBER

class TwilioClient:
    
    def __init__(self, client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)):
        
        self.client = client

    def post_sms(self, message_body, send_to=TEST_NUMBER):
        """Send a standard SMS message"""
        
        message = self.client.messages.create(
                        body=message_body,
                        from_=TWILIO_PHONE_NUMBER,
                        to=send_to
                    )
        return message
    
        
    def post_mms(self, message_body, image_url, send_to=TEST_NUMBER):
        """Send a MMS multimedia message"""
        
        message = self.client.messages.create(
                        body=message_body,
                        from_=TWILIO_PHONE_NUMBER,
                        media_url = [image_url],
                        to=send_to
                    )
        
        return message
    
    
    def create_call(self, call_to=TEST_NUMBER):
        """Create automated voice call message."""
        
        message = self.client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=call_to,
                        from_=TWILIO_PHONE_NUMBER
        )
        
        return message
        
        