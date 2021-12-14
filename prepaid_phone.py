from connector import connection_twilio, connection_sendgrid
from exceptions import PrepaidPhoneEmptyAccount, PrepaidPhoneLimitReached, PrepaidPhoneMessageContent, PrepaidPhoneImageUrl, PrepaidPhoneEmailSubject, PrepaidPhoneEmailContent


class PrepaidPhone:
    def __init__(self, limit = 100):
        self.limit = limit
        
    def get_limit(self):
        return self.limit
    
    def add_to_limit(self, add_limit):
        self.limit += add_limit
        
    def call(self, call_limit=50):
        try:
            if self.limit == 0:
                raise PrepaidPhoneEmptyAccount("You have an empty account. Call has been interrupted.")
            self.limit -= call_limit
            if self.limit < 0:
                raise PrepaidPhoneLimitReached("You have reached the limit.Re-charging phone.")
            message = connection_twilio.create_call()
            print(message)
            print("Call finished. Actual account money status: \n" + str(self.get_limit()))
        except PrepaidPhoneEmptyAccount as e:
            print(e)
            print("You have to re-charge your prepaid phone. No money detected!!!")
        except PrepaidPhoneLimitReached as e:
            print(e)
            self.add_to_limit(abs(self.limit))
            print(self.limit)
            
    def send_sms(self, message_content):
        try:
            if not type(message_content) == str:
                raise PrepaidPhoneMessageContent("A message you want to send needs to be of type String")
        except PrepaidPhoneMessageContent as e:
            print(e)
        else:
            message = connection_twilio.post_sms(message_content)
            print(message)
            
    def send_mms(self, message_content, image_url):
        try:
            if not type(message_content) == str:
                raise PrepaidPhoneMessageContent("A message you want to send needs to be of type String")
            if not type(image_url) == str:
                raise PrepaidPhoneImageUrl("The image url needs to be a string too!")
        except PrepaidPhoneMessageContent as e:
            print(e)
        except PrepaidPhoneImageUrl as e:
            print(e)
        else:
            message = connection_twilio.post_mms(message_content, image_url)
            print(message)
            
    def send_email(self, html_content, subject):
        try:
            if not type(subject) == str:
                raise PrepaidPhoneEmailSubject("Subject needs to be a string")
            if not type(html_content) == str:
                raise PrepaidPhoneEmailContent("Content/body of the email needs to be in string and can include html tags.")
        except PrepaidPhoneEmailSubject as e:
            print(e)
        except PrepaidPhoneEmailContent as e:
            print(e)
        else:
            message = connection_sendgrid.post_email(subject, html_content)
            print(message)
            print(message.status_code)
            print(message.body)
            print(message.headers)
        
            

prepaidphone = PrepaidPhone()

# prepaidphone.send_mms('This is with image', 'https://i.pinimg.com/474x/22/50/d0/2250d0104b25d5e8bde46c462822f291.jpg')

# prepaidphone.call()

prepaidphone.send_email('Sending with Twilio SendGrid is Fun','<strong>and easy to do anywhere, even with Python</strong>')