default_user = {
    "user_pin": 9878,
    "user_balance": 97432.47,
    "user_name": "Mr. John Doe"
}
print("-"*87)
print(f"{" "*32} ATM Simulation System")
while True:
    authenticated = False
    while not authenticated:
        print("-"*87)
        pin = eval(input("\nPlease enter your 4-digit PIN to login: "))
        if pin == default_user["user_pin"]:
            print("\nAccount authorized successfully!")
            authenticated = True
        else:
            print("Authentication Failed! Please try again.")
    print(f"\nWelcome to your bank account {default_user["user_name"]}")
    print(f"""
        {' '*25}--x-x-x--DASHBOARD--x-x-x-- \n
        {' '*25}1. View Account Balance
        {' '*25}2. Withdraw Cash
        {' '*25}3. Deposit Cash
        {' '*25}4. Change PIN 
        {' '*25}5. Logout & Return Card 
        """)
    
    ch = int(input("Enter your choice: "))
    if ch == 1:
        authenticated = False
        while not authenticated:
            pin = eval(input("\nPlease enter your 4-digit PIN to complete the transaction: "))
            if pin == default_user["user_pin"]:
                authenticated = True
                print("\nAccount authorized successfully!!")
                print("\nLoading your account balance...")
                print(f"\nYour current balance is Rs. {default_user["user_balance"]}")
            else:
                print("\nAuthentication Failed! Please try again.")    
    elif ch == 2:
        authenticated = False
        while not authenticated:
            pin = eval(input("\nPlease enter your 4-digit PIN to complete the transaction: "))
            if pin == default_user["user_pin"]:
                authenticated = True
                print("\nAccount authorized successfully!!")
                amount = eval(input("\nEnter amount you wish to withdraw: "))
                if amount > default_user["user_balance"]:
                    print("\nInsufficient balance! Please try with lower amount.")
                else:
                    default_user["user_balance"] = default_user["user_balance"] - amount
                    print("\nAmount withdrawn successfully.")
                    print(f"\nYour remaining balance is Rs. {default_user["user_balance"]}")
            else:
                print("\nAuthentication Failed! Please try again.") 
    elif ch == 3:
        authenticated = False
        while not authenticated:
            pin = eval(input("\nPlease enter your 4-digit PIN to complete the transaction: "))
            if pin == default_user["user_pin"]:
                authenticated = True
                print("\nAccount authorized successfully!!")
                amount = eval(input("\nEnter amount you wish to deposit: "))
                default_user["user_balance"] = default_user["user_balance"] + amount
                print("\nAmount deposited successfully")
                print(f"\nYour updated balance is Rs. {default_user["user_balance"]}")
            else:
                print("\nAuthentication Failed! Please try again.") 
    elif ch == 4:
        authenticated = False
        while not authenticated:
            old_pin = eval(input("\nPlease enter your 4-digit old PIN: "))
            if old_pin == default_user["user_pin"]:
                authenticated = True
                new_pin = eval(input("\nPlease enter your 4-digit New PIN: "))
                default_user["user_pin"] = new_pin
                print("\nPIN changed successfully.")
            else:
               print("\nIncorrect old PIN! Please try again.")
    elif ch == 5:
        print("\nLogging out...")
        print("Returning your card...")
        print("You have been logged out.")
        print("Thank you, Visit again.")
        break
    else:
        print("Invalid choice!")