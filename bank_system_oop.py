import random

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def check_balance(self):
        print({"name": self.name, "balance": self.balance})
    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            print({"name": self.name, "balance": self.balance})
        except ValueError:
            print("INVALID INPUT.")
    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Your balance isn't enough.")
        except ValueError:
            print("INVALID INPUT.")
        print("Updated Account Info:", {"name": self.name, "balance": self.balance})
banks = ["EL AHLY BANK", "CIB", "NATIONAL BANK"]
bank_name = random.choice(banks)
print("WELCOME TO", bank_name)
name = input("Enter your name: ")
while True:
    try:
        balance = float(input("Enter your initial balance: "))
        break
    except ValueError:
        print("Please enter a valid number.")
account = Account(name, balance)
while True:
    print(" Main Menu ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        account.check_balance()
    elif choice == "2":
        account.deposit()
    elif choice == "3":
        account.withdraw()
    elif choice == "4":
        print("Thank you for using our bank system!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")


