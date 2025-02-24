class BankAccount:
    def __init__(self, owner, balance=0, pin=None):
        self.owner = owner
        self.balance = balance
        self.pin = pin

    def set_pin(self, pin):
        self.pin = pin
        print(f"PIN set for {self.owner}")

    def verify_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrawn ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def show_info(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"

# Creating an account
account1 = BankAccount("John Doe", 1000)
account1.set_pin(1234)
account1.deposit(500)
account1.withdraw(300)

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
        new_account = BankAccount(name, balance)
        new_account.set_pin(pin)
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