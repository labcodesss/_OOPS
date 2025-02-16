class Account:
    def __init__(self, acc, bal):
        self.balance=bal
        self.account_number=acc


    def debit(self,amt):
        self.balance -= amt
        print(f"Rs {amt} is debited")
        print(f"total balance is {self.get_balance()}")

    def credit(self,amt):
        self.balance += amt
        print(f"Rs {amt} is credited")
        print(f"total balance is {self.get_balance()}")

    def get_balance(self):
        return self.balance    



acc1 = Account(12345, 10000)  
acc1.debit(1000)
acc1.credit(500)
acc1.credit(5100)
acc1.debit(1000)