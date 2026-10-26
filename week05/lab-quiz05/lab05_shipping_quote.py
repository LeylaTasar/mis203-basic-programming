def calculate_subtotal(quantity, unit_price):
    return quantity * unit_price

def get_discount_rate(subtotal):
    if subtotal >= 100.0:
        return 0.10
    return 0.0

def calculate_shipping_fee(subtotal):
    if subtotal >= 200.0:
        return 0.0
    return 15.0

def calculate_final_total(subtotal, discount_rate, shipping_fee):
    return (subtotal - (subtotal * discount_rate)) + shipping_fee

assert get_discount_rate(99.99) == 0.0
assert get_discount_rate(100.0) == 0.10
assert calculate_shipping_fee(200.0) == 0.0

order1_sub = calculate_subtotal(2, 25.0)
order1_disc = get_discount_rate(order1_sub)
order1_ship = calculate_shipping_fee(order1_sub)
order1_total = calculate_final_total(order1_sub, order1_disc, order1_ship)
print(f"Order 1 -> Subtotal: ${order1_sub:.2f} | Discount: {order1_disc*100}% | Shipping: ${order1_ship:.2f} | Total: ${order1_total:.2f}")

order2_sub = calculate_subtotal(5, 50.0)
order2_disc = get_discount_rate(order2_sub)
order2_ship = calculate_shipping_fee(order2_sub)
order2_total = calculate_final_total(order2_sub, order2_disc, order2_ship)
print(f"Order 2 -> Subtotal: ${order2_sub:.2f} | Discount: {order2_disc*100}% | Shipping: ${order2_ship:.2f} | Total: ${order2_total:.2f}")
