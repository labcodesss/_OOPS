class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public variable
        self.__balance = balance  # Private variable (Encapsulation)

    # Getter method to access balance
    def get_balance(self):
        return self.__balance

    # Setter method to update balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount!")

# Creating an account
account = BankAccount("123456", 1000)

# Accessing balance using the getter method
print("Current Balance:", account.get_balance())

# Depositing money
account.deposit(500)

# Withdrawing money
account.withdraw(300)

# Trying to access private balance directly (This will give an error)
# print(account.__balance)  # ❌ AttributeError
