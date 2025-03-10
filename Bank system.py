def show_balance():
    print(f"Your balance is $ {balance:.2f}")



def deposit():
    amount = float(input("Enter an amount to be deposited : "))

    if amount < 0:
        print("You cannot deposit a negative amount.")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter an amount to be withdrawn : "))
    if amount < 0:
        print("You need to draw more then 0")
        return 0

    elif amount > balance:
        print("You cannot withdraw more than your balance.")

    else:
        return amount




balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()

    elif choice == "2":
        balance += deposit()

    elif choice == "3":
        balance -= withdraw()

    elif choice == "4":
        is_running = False

    else:
        print("Invalid choice")

print("Thank you! Have a nice day!")