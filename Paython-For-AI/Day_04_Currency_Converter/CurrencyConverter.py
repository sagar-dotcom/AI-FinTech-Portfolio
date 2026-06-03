import requests # Internet se data laane ke liye

def get_exchange_rate(base_currency, target_currency):
    # Yeh ek free API hai jiske liye kisi password/key ki zarurat nahi hai
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
    
    try:
        # API ko call lagana
        response = requests.get(url)
        # API se aaye hue data (JSON) ko Python dictionary mein badalna
        data = response.json() 
        
        # Check karna ki target currency API mein available hai ya nahi
        if target_currency.upper() in data['rates']:
            rate = data['rates'][target_currency.upper()]
            return rate
        else:
            return None
            
    except Exception as e: # Agar internet nahi chal raha ya API down hai
        print("❌ Network error! Apna internet connection check karein.")
        return None

# --- MAIN MENU ENGINE ---
def main():
    print("🌍 Welcome to Live FinTech Currency Converter 🌍")
    
    while True:
        print("\n1. Convert Currency (e.g., USD to INR)")
        print("2. Exit")
        
        choice = input("Apni choice batao (1/2): ")
        
        if choice == '1':
            base = input("Base Currency (e.g., USD, EUR, GBP): ").strip().upper()
            target = input("Target Currency (e.g., INR, AED): ").strip().upper()
            
            try:
                amount = float(input(f"Kitne {base} convert karne hain? : "))
            except ValueError:
                print("❌ Galat input! Sirf numbers type karein.")
                continue # Agar user ne number ki jagah text daala toh loop wapas shuru hoga
            
            print("⏳ Live rate fetch kar rahe hain... please wait.")
            
            # API function ko call karna
            rate = get_exchange_rate(base, target)
            
            if rate:
                converted_amount = amount * rate
                print(f"✅ Live Rate: 1 {base} = {rate} {target}")
                print(f"💰 Total Amount: {amount} {base} = {round(converted_amount, 2)} {target}")
            else:
                print("❌ Currency code galat hai ya API usko support nahi karti.")
                
        elif choice == '2':
            print("Converter band ho raha hai. Bye! 👋")
            break
        else:
            print("❌ Galat choice! Sirf 1 ya 2 type karein.")

# Program Start
if __name__ == "__main__":
    main()