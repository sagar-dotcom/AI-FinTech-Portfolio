class BankAccount:
    """Blue print for Bank Account"""
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def account_details(self):
        print(f"--- Account Details ---")
        print(f"Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance}")
    
    # Object creation
sagar_account = BankAccount("Sagar", 5000)

# Method callimg
sagar_account.account_details()
        