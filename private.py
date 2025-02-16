class Account:
    def __init__(self, account_number, account_psw):
        self.number=account_number
        self.__psw= account_psw
        #(__) is used for private cant be accessed outside class

    def reset_psw(self):
         print(self.__psw)   

s1=Account("1234","mouna")        
print(s1.number)
print(s1.reset_psw())