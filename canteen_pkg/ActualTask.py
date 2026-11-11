# CANTEEN BILLING SYSTEM

# Function 1: Add item to cart
def add_item(cart, item_name, price, quantity):
    if price <= 0 or quantity <= 0:
        raise ValueError("Price and quantity must be positive")

    item = {
        "name": item_name,
        "price": price,
        "quantity": quantity
    }

    cart.append(item)


# Function 2: Calculate subtotal
def calculate_bill(cart):
    subtotal = 0

    for item in cart:
        amount = item["price"] * item["quantity"]
        subtotal += amount

    return subtotal


# Function 3: Apply discount
def apply_discount(subtotal):
    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    return discount


# Function 4: Calculate tax
def calculate_tax(amount):
    tax = amount * 0.05
    return tax


# Function 5: Display final bill
def display_bill(cart, subtotal, discount, tax, total):
    print("\n==============================================")
    print("                 CANTEEN BILL")
    print("==============================================")

    print(f"{'Item':<12}{'Price':>8}{'Qty':>6}{'Amount':>12}")
    print("----------------------------------------------")

    for item in cart:
        amount = item["price"] * item["quantity"]

        print(f"{item['name']:<12}{item['price']:>8}"
              f"{item['quantity']:>6}{amount:>12.2f}")

    print("----------------------------------------------")
    print(f"Subtotal:              Rs. {subtotal:.2f}")
    print(f"Discount:              Rs. {discount:.2f}")
    print(f"GST (5%):              Rs. {tax:.2f}")
    print("----------------------------------------------")
    print(f"FINAL AMOUNT:          Rs. {total:.2f}")
    print("==============================================")
    print("          THANK YOU! VISIT AGAIN!")
    print("==============================================")
