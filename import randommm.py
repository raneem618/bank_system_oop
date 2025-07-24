import random
def check_balance(name, balance):
    value = {"name": name, "balance": balance}
    print(value)

def deposit(balance):
    try:
        amount = float(input("Enter amount to deposite :"))
        balance+=amount
    except ValueError:
        print("INVALID INPUT.")
    value = {"name": name, "balance": balance}
    print(value)
    return balance

def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Your balance isn't enough.")
    except ValueError:
        print("INVALID INPUT.")
    value = {"name": name, "balance": balance}
    print("Updated Account Info:", value)
    return balance

banks = ["EL AHLY BANK", "CIB", "NATIONAL BANK"]
x = random.choice(banks)
print("WELCOME TO", x)

name = input("Enter your name: ")
while True:
    try:
        balance = float(input("Enter your initial balance: "))
        break
    except ValueError:
        print("Please enter a valid number.")

while True:
    print(" Main Menu ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        check_balance(name, balance)
    elif choice == "2":
        balance = deposit(balance)
    elif choice == "3":
        balance = withdraw(balance)
    elif choice == "4":
        print("Thank you for using our bank system!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
