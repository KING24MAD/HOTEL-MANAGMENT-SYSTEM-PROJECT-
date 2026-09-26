# Display the hotel menu and let the customer place an order.
menu = {
    'pizza' : 250,
    'burger' : 150,
    'pasta' : 200,
    'sandwich' : 100,
    'coffee' : 50,
}

# now we will greet the customer and show the menu to them
print("Welcome to our Hotel Management System!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: Rs {price}")

order_total = 0

item_1 = input("Please enter the first item you would like to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Current total: Rs {order_total}")
else:
    print(f"Sorry, {item_1} is not on the menu.")

another_item = input("Would you like to order another item? (yes/no): ")
if another_item.lower() == 'yes':
    item_2 = input("Please enter the second item you would like to order: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} added to your order. Current total: Rs {order_total}")
    else:
        print(f"Sorry, {item_2} is not on the menu.")

print(f"Your final order total is: Rs {order_total}")

        
