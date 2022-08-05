#to do, refactoring

from os import close
from prepaid_phone import PrepaidPhone
from data_storage import sms_data, mms_data, voice_data, email_data, start_data, exit_data

class start:

    welcome_message = """
        Welcome to the PrePaid phone simulator.
        You can send an sms, mms, make a voice call or send an email here :)\n
    """
    print(welcome_message)
    choice = str(input("To start, just type start or run or anything like that :)\n"))

    if choice in start_data:
        run = True
    else:
        print("Sorry, input has not been reocgnized, try again.")

    while run:
        print("\nFirst, you need to charge your prepaid phone.\n")
        print("Pricing: Voice call: 50, SMS: 25, MMS: 25, Email: Free, just needs internet connection :)\n")
        get_and_charge = int(input("For how much would you like to charge your prepaid phone?\n"))
        if get_and_charge < 0:
            print("Sorry, but you cannot charge a phone with a negative value.\n")
        else:
            prepaidphone = PrepaidPhone(get_and_charge)
        while True:
            if prepaidphone:
                print("\nActions: SMS, MMS, Voice, Email\n")
                action = input("So, what would you like to do now? Just type the action name: SMS, MMS, Voice or Email.\n")
            else:
                print("Sorry, I did not catch that, please try again.\n")
            if action in sms_data:
                print("\nTo send a SMS, you need to type the message you would like to send, and also the number you would like to send it to.\n")
                number = str(input('Type the number with country extensions (e.g. +48 for Poland following the phone number)\n'))
                message_content = str(input('Type the text message you want to send out.\n'))
                prepaidphone.send_sms(message_content, number)
            elif action in mms_data:
                print("\nTo send a MMS, you need to type the message you would like to send, and also the number you would like to send it to and the image url to show :).\n")
                number = str(input('Type the number with country extensions (e.g. +48 for Poland following the phone number)\n'))
                message_content = str(input('Type the text message you want to send out.\n'))
                image_url = str(input("Provide the url to the image you would like to send within the MMS.\n"))
                prepaidphone.send_mms(message_content,image_url, number)
            elif action in voice_data:
                print("\nTo create an automated voice call you just need to type the number")
                call_to = str(input('Type the number with country extensions (e.g. +48 for Poland following the phone number)'))
                prepaidphone.call(call_to)
            elif action in email_data:
                print("\nTo send an email you need to provide the text, the subject and the mail you would like to send it to.")
                html_content = str(input('Type the text:\n'))
                subject = str(input('Type the subject:\n'))
                to_emails = str(input('Type the emails to send to:\n'))
                prepaidphone.send_email(html_content, subject, to_emails)
            elif action in exit_data:
                close
            else:
                print("No action found, try again.")
            
    
        