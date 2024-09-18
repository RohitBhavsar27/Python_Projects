catalog = {
    1:"Rice", 2:"Flour", 3:"Sugar", 4:"Milk", 5:"Oil", 6:"Tea", 7:"Coffee", 8:"Juice", 9:"Soda", 10:"Shampoo", 11:"Toothpaste", 12:"Soap", 13:"Lotion", 14:"Detergent", 15:"Dishwash Liquid", 16:"Tissue Paper", 17:"Garbage Bags", 18:"LED Bulbs", 19:"Extension Cord", 20:"Batteries", 21:"Phone Charger"
}

price = {
    1: 100, 2: 50, 3: 60, 4: 45, 5: 120, 6: 90, 7: 150, 8: 80, 9: 30, 10: 180, 11: 75, 12: 40, 13: 200, 14: 150, 15: 90, 16: 30, 17: 60, 18: 120, 19: 250, 20: 50, 21: 300
}

discount = {
    1:20, 2:20, 3:20, 4:20, 5:20,
    6:10, 7:10, 8:10, 9:10,
    10:8, 11:8, 12:8, 13:8,
    14:15, 15:15, 16:15, 17:15,
    18:5, 19:5, 20:5, 21:5 
}

order = {}

print("-"*106)
print(f"{" "*45} DMart Pune")
print("-"*106)

while True:
    print(f"""
        {' '*32}-x-x-x--CATALOG--x-x-x- \n
    1.Rice                      2.Flour                 3.Sugar                         4.Milk\n
    5.Oil                       6.Tea                   7.Coffee                        8.Juice\n
    9.Soda                      10.Shampoo              11.Toothpaste                   12.Soap\n
    13.Lotion                   14.Detergent            15.Dishwash Liquid              16.Tissue Paper\n
    17.Garbage Bags             18.LED Bulbs            19.Extention Cord               20.Batteries\n
    21.Phone Charger
    """)
    
    item = eval(input("Enter Your Choice: "))
    if item > len(catalog):
        print("Invalid Choice! Please choose from Catalog.")
        break 
    qty = eval(input("Enter Quantity: "))
    order[item] = qty
    ch = input("Do you Want to continue(y/n): ").lower()
    if ch == 'n':
        print("-"*106)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Item Name", "Quantity", "Price", "Discount", "Amount"))
        print("-"*106)
        total_amount = 0
        for item, quantity in order.items():
            discounted_price = price[item] - float(price[item]*discount[item]/100)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(catalog[item], quantity, price[item], discount[item], quantity*discounted_price))
            print("-"*106)
            total_amount += quantity*discounted_price
        print("|{:^83}|{:^20}|".format("Your Total Bill", total_amount))
        print("-"*106)
        print("\nThank You! Visit Again.")
        break
