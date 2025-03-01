class BankAccount:
    def __init__(self, account_holder, balance=0, pin=None):
        self.account_holder = account_holder  
        self._balance = balance  
        self.__pin = pin  
    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount > 0:
            self._balance = amount
        else:
            print("Amount must be positive")

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.account_holder} deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"{self.account_holder} withdrawn ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current balance: ${self._balance}")

    def show_info(self):
        return f"Owner: {self.account_holder}, Balance: ${self._balance}"

# Creating an account
account1 = BankAccount("John Doe", 1000, 1234)

# Accessing the public attribute
print(f"Account Holder: {account1.account_holder}")  

# Trying to access the protected attribute
print(f"Balance (protected): {account1._balance}")  

# Trying to access the private attribute (will raise an AttributeError)
try:
    print(f"PIN (private): {account1.__pin}")
except AttributeError as e:
    print(e)  

# Using the getter method
print(f"Balance (getter): {account1.get_balance()}") 

# Using the setter method
account1.set_balance(1500)
print(f"Updated Balance (setter): {account1.get_balance()}")  

# Verifying the PIN
print(f"PIN verification (correct): {account1.verify_pin(1234)}")  
print(f"PIN verification (incorrect): {account1.verify_pin(4321)}")  

accounts = []

while True:
    print("Menu")
    print("1. List accounts")
    print("2. Create account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    menu = input("Select menu: ")
    if menu == "1":
        for index, account in enumerate(accounts):
            print(f"{index} - {account.show_info()}")

    elif menu == "2":
        name = input("Insert name: ")
        balance = int(input("Insert balance: "))
        pin = int(input("Set PIN: "))
        new_account = BankAccount(name, balance, pin)
        accounts.append(new_account)

    elif menu == "3":
        index = int(input("Choose account index: "))
        pin = int(input("Enter PIN: "))
        if accounts[index].verify_pin(pin):
            amount = int(input("Insert deposit amount: "))
            accounts[index].deposit(amount)
        else:
            print("Incorrect PIN")

    elif menu == "4":
        index = int(input("Choose account index: "))
        pin = int(input("Enter PIN: "))
        if accounts[index].verify_pin(pin):
            amount = int(input("Insert withdraw amount: "))
            accounts[index].withdraw(amount)
        else:
            print("Incorrect PIN")

    elif menu == "5":
        break