menu = {
    1: "Poha",
    2: "Idli-Sambar",
    3: "Vada-Pav",
    4: "Vada-Sambar",
    5: "Tea",
    6: "Coffee"
}

price = {
    1: 20,
    2: 30,
    3: 15,
    4: 30,
    5: 12,
    6: 15
}

order = {}

print("-"*85)
print(f"{' '*37} Taj Hotel")
print("-"*85)
while True:
    print(f"""
        {' '*32}Menu \n
        {' '*20}1. Poha         2. Idli-Sambar
        {' '*20}3. Vada-Pav     4. Vada-Sambar
        {' '*20}5. Tea          6. Coffee
        """)
    item = eval(input("Enter Your Choice: "))
    if item > len(menu):
        print("Invalid Choice! Please choose from Menu.")
        break 
    qty = eval(input("Enter Quantity: "))
    order[item] = qty
    ch = input("Do you Want to continue(y/n): ").lower()
    if ch == 'n':
        print("-"*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("Item Name", "Quantity", "Price", "Amount"))
        print("-"*85)
        total_amount = 0
        for item, quantity in order.items():
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(menu[item], quantity, price[item], quantity*price[item]))
            print("-"*85)
            total_amount += price[item] * quantity
        print("|{:^62}|{:^20}|".format("Your Total Bill", total_amount))
        print("-"*85)
        print("\nThank You! Visit Again.")
        break