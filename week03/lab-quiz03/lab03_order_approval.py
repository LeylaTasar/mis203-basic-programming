order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
member = input("Is the customer a member? (yes/no): ").lower()

if requested_quantity <= 0:
    print("Order rejected: invalid quantity.")

elif requested_quantity > available_stock:
    print("Order rejected: insufficient stock.")

elif order_amount < 0:
    print("Order rejected: invalid order amount.")

else:
    final_price = order_amount

    if member == "yes" and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Order approved: Member discount applied.")
    elif member == "yes":
        print("Order approved: No discount because order is below 500 TRY.")
    else:
        print("Order approved: No member discount.")

    print(f"Final price: {final_price:.2f} TRY")

