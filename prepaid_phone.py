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

class PrepaidPhone:
    def __init__(self, limit = 100):
        self.limit = limit
        
    def get_limit(self):
        return self.limit
    
    def add_to_limit(self, add_limit):
        self.limit += add_limit
        
    def call(self, call_limit):
        try:
            if self.limit == 0:
                raise PrepaidPhoneEmptyAccount("You have an empty account. Call has been interrupted.")
            self.limit -= call_limit
            if self.limit < 0:
                raise PrepaidPhoneLimitReached("You have reached the limit.Re-charging phone.")
            print("Call finished. Actual account money status: \n" + str(self.get_limit()))
        except PrepaidPhoneEmptyAccount as e:
            print(e)
            print("You have to re-charge your prepaid phone. No money detected!!!")
        except PrepaidPhoneLimitReached as e:
            print(e)
            self.add_to_limit(abs(self.limit))
            print(self.limit)

prepaidphone = PrepaidPhone()
prepaidphone.call(60)
print("Make another call")
prepaidphone.call(60)
