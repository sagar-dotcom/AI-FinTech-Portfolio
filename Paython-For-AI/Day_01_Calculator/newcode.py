# Calculator created by Sagar Agarwal
# Master Finance Calculator - Core Architecture

# 1. Basic Math Function
def basic_math(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

# 2. EMI Calculator Function
def calculate_emi(loan_amt, int_rate, duration_years):
    monthly_int_rate = int_rate / (12 * 100) 
    total_months = int(duration_years * 12)
    
    if monthly_int_rate == 0: # If interest rate is 0
        emi = loan_amt / total_months
    else:
        emi = loan_amt * monthly_int_rate * ((1 + monthly_int_rate)**total_months) / (((1 + monthly_int_rate)**total_months) - 1)
        
    total_payment = emi * total_months
    total_interest = total_payment - loan_amt
    
    return round(emi, 2), round(total_payment, 2), round(total_interest, 2)

# 3. Bill Splitter Function
def split_bill(total_amt, tip_percent, total_members):
    if total_members <= 0:
        return "Error: Members must be at least 1"
        
    total_tip = (total_amt * tip_percent) / 100
    total_amount_with_tip = total_amt + total_tip
    per_person_amt = total_amount_with_tip / total_members
    
    return round(per_person_amt, 2), round(total_tip, 2), round(total_amount_with_tip, 2)

# 4. GST Calculator Function
def calculate_gst(base_amt, gst_rate):
    gst_amount = base_amt * (gst_rate / 100)
    total_amount = base_amt + gst_amount
    return round(gst_amount, 2), round(total_amount, 2)

# Main Menu Logic (Yeh console ke liye hai, App mein iski jagah UI aayega)
def main():
    while True:
        print("\n" + "="*35)
        print(" MASTER FINANCE CALCULATOR")
        print ("*"*35)
        print("1. Basic Math(add/sub/mul/div)")
        print("2. EMI Calculator")
        print("3. Bill Splitter & Tip Manager")
        print("4. Tax / GST Calculator")
        print("5. Exit")
        print("*"*35)

        choice = input("Enter your choice (1 to 5): ")
        
        if choice == '1':
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
            op = input("Operator (+, -, *, /): ")
            print(f"Result: {basic_math(n1, n2, op)}")
            
        elif choice == '2':
            loan = float(input("Loan amount: "))
            rate = float(input("Annual Interest Rate (%): "))
            time = float(input("Time (Years): "))
            emi, total_pay, total_int = calculate_emi(loan, rate, time)
            print(f"Monthly EMI: {emi}\nTotal Payment: {total_pay}\nTotal Interest: {total_int}")
            
        elif choice == '3':
            amt = float(input("Total Bill Amount: "))
            tip = float(input("Tip in %: "))
            members = int(input("Total members: "))
            result = split_bill(amt, tip, members)
            if isinstance(result, str): # Error handling
                print(result)
            else:
                per_person, total_tip, total_amt = result
                print(f"Per Person: {per_person}\nTotal Tip: {total_tip}\nTotal Payment: {total_amt}")
                
        elif choice == '4':
            base = float(input("Base amount: "))
            rate = float(input("GST rate (%): "))
            gst_amt, total = calculate_gst(base, rate)
            print(f"GST Amount: {gst_amt}\nTotal Amount: {total}")
            
        elif choice == '5':
            print("Thank you for using Master Finance Calculator!")
            break
        else:
            print("\n[ERROR] Invalid input! Please enter a number between 1 and 5.")

# Program ko run karne ke liye
if __name__ == "__main__":
    main()