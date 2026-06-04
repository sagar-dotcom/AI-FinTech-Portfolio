
        

balance = 10000
daily_limit = 5000
def withdrawal():
    global balance
    global daily_limit
    amount = float(input("Please enter withdrwal amt :"))
    if amount % 100 != 0:
        print("Emter amount should be multiple of 100")
    elif amount > balance:
        print("Enter amount is greater then your balance amount")
    elif amount >daily_limit:
        print("enter amount is greater then daily limit")
    else:
        balance -= amount
        print(f"✅ Total remaining balance ₹ {balance}. ")
def main():
    global balance
    global daily_limit
    while True:
        # Loop ke andar wali lines ko 4 spaces aage rakho
        choice = input("W for Withdraw, D for Deposit, B for Balance, Q for Quit: ").upper()
        
        if choice == 'Q':
            break
        elif choice == 'W':
            withdrawal() 
        elif choice == 'D':
            # Deposit logic yahan likho
            amount = float(input("Deposit amount: "))
            balance += amount
            print(f"✅ ₹{amount} deposit ho gaye. Naya balance: ₹{balance}")
        elif choice == 'B':
            print(f"💰 Current Balance: ₹{balance}")
        else:
            print("❌ Invalid choice!")

# Program run karne ke liye
main()