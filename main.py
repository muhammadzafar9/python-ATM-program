"""Banking program application."""

from utils import show_balance

def get_float_input(prompt):
    """Gets float input from the user with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def deposit():
    """Handles deposit transactions."""
    print("*********************")
    amount = get_float_input("Enter an amount to be deposited: ")
    print("*********************")

    if amount <= 0:
        print("*********************")
        print("Amount must be greater than 0.")
        print("*********************")
        return 0
    return amount

def withdraw(balance):
    """Handles withdrawal transactions."""
    print("*********************")
    amount = get_float_input("Enter amount to be withdrawn: ")
    print("*********************")

    if amount <= 0:
        print("*********************")
        print("Amount must be greater than 0.")
        print("*********************")
        return 0
    elif amount > balance:
        print("*********************")
        print("Insufficient funds.")
        print("*********************")
        return 0
    return amount

def main():
    """Main function to run the banking program."""
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")
# switch statement used to be here
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
            show_balance(balance) # Show balance after deposit
        elif choice == '3':
            withdrawal_amount = withdraw(balance)
            if withdrawal_amount > 0:
                balance -= withdrawal_amount
                show_balance(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("Invalid choice. Please enter a number between 1 and 4.")
            print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

if __name__ == '__main__':
    main()