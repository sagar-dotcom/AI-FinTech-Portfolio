class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        # Parent (BankAccount) ko initialize kar rahe hain
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied. New Balance: ${self.balance:.2f}")