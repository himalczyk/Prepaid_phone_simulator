class PrepaidPhoneLimitReached(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg
    
class PrepaidPhoneEmptyAccount(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg
    
class PrepaidPhoneMessageContent(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg
    
class PrepaidPhoneImageUrl(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg
    
class PrepaidPhoneEmailSubject(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg
    
class PrepaidPhoneEmailContent(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg