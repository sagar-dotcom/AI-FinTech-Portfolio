# Calculator created by Sagar Agarwal
# Master Finance Calculator - Core Architecture

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

    #Take input from user
    choice = input("Enter your choice (1 to 5): ")
    
    if choice == '1':
        first_input = float(input("Please enter your first number:" ))
        second_input = float(input("Please enter your second number:" ))
        operator = input("Enter operation (+, -, *, /): ")
        if operator == "+":
            result = first_input + second_input
            print(f"Result: {result}")
        elif operator == "-":
            result = first_input - second_input
            print(f"Result: {result}")
        elif operator == "*":
            result = first_input * second_input
            print(f"Result: {result}")
        elif operator == "/":
            if second_input == 0:
                print("Cannot divide by zero")
            else:
                result = first_input / second_input
                print(f"Result: {result}")
        else:
             print("Invalid operator")
    #Choice 2 for EMI Calculator
    elif choice == "2":      
        loan_amt = float(input("Enter your loan amount: "))
        int_rate = float(input("Annual Interest Rate (%): "))
        duration = float(input("Enter Time (Years): "))
        monthly_int_rate = int_rate / (12 * 100) 
        total_month = int(duration * 12)
        #Formula of EMI Calculator
        emi = loan_amt * monthly_int_rate * (1 + monthly_int_rate)**total_month/((1 + monthly_int_rate)**total_month - 1)
        print(f"Monthly EMI: {emi:.2f}")
        total_payment = emi * total_month
        total_interest = total_payment - loan_amt
        print(f"Total Payment: {total_payment:.2f}")
        print(f"Total Interest: {total_interest:.2f}")
    elif choice == "3":
        total_amt = float(input("Enter Total Bill Amount: "))
        tip = float(input("Enter Tip in %: "))
        while True:
            total_member = int(input("Total members: "))
            if total_member <= 0:
             print("Cannot divide by zero 0r less then zero")
            else:
                break
        total_tip = (total_amt * tip)/100
        per_person_amt = (total_amt + total_tip)/total_member
        Total_amount = total_amt + total_tip
        print(f"Total Payment by one person: {per_person_amt:.2f}")
        print(f"Total Tip: {total_tip:.2f}")
        print(f"Total Payment: {Total_amount:.2f}")
    elif choice == "4":
        base_amt = float(input("Enter base amount: "))
        gst_rate = float(input("Enter GST rate (%) (e.g., 5, 12, 18, 28): "))
        
        gst_amount = base_amt * (gst_rate / 100)
        total_amount = base_amt + gst_amount
        
        print(f"\nGST Amount: {gst_amount:.2f}")
        print(f"Total Amount (Inclusive of GST): {total_amount:.2f}")
    elif choice == "5":
        print("Thank you for using Master Finance Calculator!")
        break
    else:
        print("\n[ERROR] Invalid input! Please enter a number between 1 and 5.")
