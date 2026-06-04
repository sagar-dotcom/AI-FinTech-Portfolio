#Auther by Sagar Agarwal
import json
FILE_NAME = "bank_data.json"   
def load_balance():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data["balance"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 10000
def save_balance(amount):
    with open(FILE_NAME, "w") as file:
        json.dump({"balance": amount}, file)
balance = load_balance()
daily_limit = 5000
def withdrawal():
    global balance
    amount = float(input("Please enter withdrwal amt :"))
    if amount % 100 != 0:
        print("Emter amount should be multiple of 100")
    elif amount > balance:
        print("Enter amount is greater then your balance amount")
    elif amount >daily_limit:
        print("enter amount is greater then daily limit")
    else:
        balance -= amount
        save_balance(balance)
        print(f"✅ Total remaining balance ₹ {balance}. ")
def main():
    global balance
    while True:
        # Loop Dtart
        choice = input("W for Withdraw, D for Deposit, B for Balance, Q for Quit: ").upper()      
        if choice == 'Q':
            break
        elif choice == 'W':
            withdrawal() 
        elif choice == 'D':
            # Deposit logic
            amount = float(input("Deposit amount: "))
            balance += amount
            save_balance(balance)
            print(f"✅ ₹{amount} Amount deposited: ₹{balance}")
        elif choice == 'B':
            print(f"💰 Current Balance: ₹{balance}")
        else:
            print("❌ Invalid choice!")

# Program run from here
main()