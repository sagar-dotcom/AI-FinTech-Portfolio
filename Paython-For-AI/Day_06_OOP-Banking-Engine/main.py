from bank_engine import SavingsAccount

def run_atm():
    # Account setup
    user_acc = SavingsAccount("Sagar", 1000)
    
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Apply Interest")
        print("5. Exit")
        
        choice = input("Select option: ")
        
        if choice == '1':
            print(f"Balance: ${user_acc.get_balance()}")
        elif choice == '2':
            amt = float(input("Enter amount to deposit: "))
            user_acc.deposit(amt)
        elif choice == '3':
            amt = float(input("Enter amount to withdraw: "))
            user_acc.withdraw(amt)
        elif choice == '4':
            user_acc.apply_interest()
        elif choice == '5':
            print("Thank you for using the System!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    run_atm()