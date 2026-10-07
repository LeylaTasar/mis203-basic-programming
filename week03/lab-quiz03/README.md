# Lab 03 - Order Approval

## Description

This program checks whether an order can be approved based on:

- Order amount
- Available stock
- Requested quantity
- Customer membership status

Invalid quantities and orders with insufficient stock are rejected.

Members receive a **10% discount** on approved orders of **500 TRY or more**.

## Test Table

| Test Case | Order Amount | Available Stock | Requested Quantity | Member | Expected Result |
|-----------|--------------|-----------------|--------------------|--------|-----------------|
| 1 - Boundary | 500 TRY | 10 | 5 | Yes | Approved, 10% discount, final price 450 TRY |
| 2 - Invalid Quantity | 600 TRY | 10 | 0 | Yes | Rejected - invalid quantity |
| 3 - Insufficient Stock | 700 TRY | 3 | 5 | No | Rejected - insufficient stock |

## Test Run

I tested the program with an order amount of 500 TRY, 10 units of available stock, and a requested quantity of 5. The customer was a member, so the order was approved and the 10% discount was applied.

## Change After Testing

After testing, I checked the boundary condition for exactly 500 TRY and made sure that the member discount is applied correctly at this amount.

## Requirements

The program uses:

- `if`, `elif`, and `else`
- Logical operators
- Input validation
- Stock checking
- Membership checking
- 10% member discount for approved orders of at least 500 TRY
