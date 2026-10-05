order_amount = float(input("Enter the order amount (TRY): "))
available_stock = int(input("Enter the available stock: "))
requested_quantity = int(input("Enter the requested quantity: "))
is_member_input = input("Is the customer a member? (y/n): ").strip().lower()

is_member = is_member_input == 'y'

if requested_quantity <= 0:
    print("Order Rejected: Invalid quantity requested.")
elif requested_quantity > available_stock:
    print("Order Rejected: Insufficient stock.")
else:
    
    final_price = order_amount
    
    if is_member and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Order Approved: 10% member discount applied.")
    else:
        print("Order Approved: No discount applied.")
        
    print(f"Final Price: {final_price:.2f} TRY")
