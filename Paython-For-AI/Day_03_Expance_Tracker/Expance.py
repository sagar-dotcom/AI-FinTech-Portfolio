
import json
FILE_NAME = "expenses.json"

def load_expenses():
    # 'try-except' use kar rahe hain taaki agar pehli baar mein file na mile toh error na aaye
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file) # Purana data file se utha liya
    except FileNotFoundError:
        return [] # Agar file nahi mili, toh ek khali list ban jayegi

# Program start hote hi purana data load ho jayega
expenses = load_expenses()

# 2. FUNCTIONS
def save_expenses():
    # Naya function: Jab bhi list update hogi, yeh usko file mein likh dega
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file)
# 3. FUNCTIONS
def add_expense():
    item = input("Expance details (e.g., Food, Rent): ")
    amount = float(input("How much spand : "))
    expenses.append({"item": item, "amount": amount})
    save_expenses() 
    print(f"✅ {item} ka kharcha add ho gaya!\n")
# 4. FUNCTIONS
def view_expenses():
    print("\n--- 💸 total Expance---")
    total = 0
    # List ke andar For-Loop lagakar ek-ek item print karna
    for exp in expenses:
        print(f"Item: {exp['item']} | Amount: ₹{exp['amount']}")
        total += exp['amount'] # Total amount calculate karna
        
    print(f"---------------------------\n💰 Total Kharcha: ₹{total}\n")
def main():
    while True: # Loop will run till user not break
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Exit")
        choice = input("Apni choice batao (1/2/3): ")
        
        # If-Else condition se user ki choice handle karna
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Expense Tracker band ho raha hai. Bye! 👋")
            break # Loop ko rokne ke liye
        else:
            print("❌ Galat choice! Sirf 1, 2, ya 3 type karein.\n")

# Program ko start karne ke liye function ko call karna
main()
