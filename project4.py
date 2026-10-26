
# Simple ATM Simulator

PIN = "1234"
balance = 5000

def check_balance():
    print("Current Balance: Rs.", balance)

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        print("Deposit successful!")
    else:
        print("Enter a valid amount.")

def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrawal successful!")

def atm():
    attempts = 3

    while attempts > 0:
        user_pin = input("Enter your ATM PIN: ")

        if user_pin == PIN:
            print("\nLogin successful!")
            break
        else:
            attempts -= 1
            print("Wrong PIN! Attempts left:", attempts)

    if attempts == 0:
        print("Account locked. Try again later.")
        return

    while True:
        print("\n===== SIMPLE ATM =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid choice!")

atm()
