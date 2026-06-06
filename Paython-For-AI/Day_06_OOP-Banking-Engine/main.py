from bank_engine import SavingsAccount

# Logic yahan chal raha hai
print("--- Starting FinTech Banking System ---")

# Object create kar rahe hain
my_savings = SavingsAccount("Sagar", 1000)

# Operations perform kar rahe hain
my_savings.deposit(500)
my_savings.apply_interest()

print("--- System Operations Complete ---")