
balance = 0.0
transactions = []

def check_balance(balance):
        print(f"Your current balance is: Ksh{balance:.2f}.")

def deposit_money(balance):
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            return balance
        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print(f"Your new balance is: Ksh{balance:.2f}.")
        else:
            print("Invalid deposit amount.")
        transactions.append(f"Deposited Ksh{amount:.2f}")
        return balance

def withdraw_money(balance):
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            return balance
        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print(f"Your new balance is: Ksh{balance:.2f}.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")
        transactions.append(f"Withdrew Ksh{amount:.2f}")
        return balance

def transaction_history(transactions):
        if transactions:
            print("Transaction History:")
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions yet.")

def exit_program():
        print("Thank you for using Pheo's bank. Goodbye!")
        exit()

while True:
    try:
        pin = (input("Enter your 4-digit PIN: "))
    except ValueError:
        print("Invalid input. Please enter a 4-digit PIN.")
        continue
    if pin == "1234":
        print("=======Welcome to Pheo's bank🤗=======")
        print("")
        print("1. Check Balance")
        print("2. Deposit Money")   
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        print("")
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a valid option.")
            continue
        if option == 1:
            check_balance(balance)
        elif option == 2:
            balance = deposit_money(balance)
        elif option == 3:
            balance = withdraw_money(balance)
        elif option == 4:
            transaction_history(transactions)
        elif option == 5:
            exit_program()
    else:
        print("Incorrect PIN. Please try again.")
        continue
    

    