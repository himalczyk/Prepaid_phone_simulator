import os
from dotenv import load_dotenv

load_dotenv()
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_BASE_URL = os.getenv('TWILIO_BASE_URL')
TEST_NUMBER = os.getenv('TEST_NUMBER')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
TEST_EMAIL = os.getenv('TEST_EMAIL')
TEST_SEND_TO_EMAIL = os.getenv('TEST_SEND_TO_EMAIL')