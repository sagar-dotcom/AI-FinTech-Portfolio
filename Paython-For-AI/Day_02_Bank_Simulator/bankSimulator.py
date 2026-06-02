#Bank Simulator project created by Sagar Agarwal

def Show_manu():
    print("/n" + "="*30)
    print("Our Fintach Bank Simulator")
    print("="*30)
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")
    print("-" * 30)

def deposit_money(balance, amount):
    if amount > 0:
        balance += amount
        print(f"✅ Success ₹ {amount} deposited. ")
        return balance
    else:
        print("❌ Invalid amount! Please enter a positive number.")
        return balance
def withdraw_money(balance, amount):
    if amount <= 0:
        print("❌ Invalid amount! Please enter a positive number.")
    elif amount > balance:
        print(f"❌ Transaction Failed! Insufficient balance. Your balance is ₹{balance}")
    else:
        balance -= amount
        print(f"✅ Success! ₹{amount} withdrawn.")
    return balance

def main():
    # Keep Account Balance 0 in starting
    account_balance = 0.0

    while True:
        Show_manu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            amount_deposit = float(input("Plsease enter your deposit Amount :"))
            account_balance = deposit_money(account_balance, amount_deposit)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: ₹"))
            account_balance = withdraw_money(account_balance, amount)
            
        elif choice == '3':
            print(f"\n💰 Your Current Balance is: ₹{account_balance}")
        
        elif choice == '4':
            print("\n🙏 Thank you for using Apna FinTech Bank. Have a great day!")
            break
        else:
            print("❌ Invalid Option! Please select a valid number from 1 to 4.")

# We will start our program from here
if __name__ == "__main__":
    main()