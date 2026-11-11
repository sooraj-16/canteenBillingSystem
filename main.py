
# MAIN PROGRAM - CANTEEN BILLING SYSTEM

from canteen_pkg import (
    add_item,
    calculate_bill,
    apply_discount,
    calculate_tax,
    display_bill
)

# Food menu
menu = {
    1: ("Idli", 30),
    2: ("Dosa", 50),
    3: ("Poori", 40),
    4: ("Meals", 100),
    5: ("Tea", 15),
    6: ("Coffee", 20)
}

# Empty shopping cart
cart = []

print("================================")
print("       WELCOME TO CANTEEN")
print("================================")

print("\nAVAILABLE FOOD ITEMS")

for number, item in menu.items():
    print(f"{number}. {item[0]} - Rs. {item[1]}")

# Selecting items
while True:
    try:
        choice = int(input("\nEnter item number (0 to finish): "))

        if choice == 0:
            break

        if choice not in menu:
            print("Invalid item number!")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

        name, price = menu[choice]

        add_item(cart, name, price, quantity)

        print("Item added successfully!")

    except ValueError:
        print("Please enter a valid number!")

# Generate bill
if len(cart) == 0:
    print("\nNo items ordered.")

else:
    subtotal = calculate_bill(cart)
    discount = apply_discount(subtotal)
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount)
    total = taxable_amount + tax

    display_bill(cart, subtotal, discount, tax, total)
