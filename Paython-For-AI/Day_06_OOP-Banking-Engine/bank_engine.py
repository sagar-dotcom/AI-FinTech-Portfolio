class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Yahan direct __balance use mat karo!
        # Parent class ke 'get_balance()' method ko use karo.
        interest = self.get_balance() * self.interest_rate
        print(f"Applying interest: ${interest:.2f}")
        self.deposit(interest) # Parent ka deposit method use karo