Lab 03: Order Approval Policy

Boundary Test Cases (Stretch Task)

The following table shows the inputs and expected results for the 500 TRY discount boundary cases:

Test Case

Order Amount (TRY)

Available Stock

Requested Qty

Member?

Expected Result

Just below 500

499.99

10

2

y

Order Approved: No discount applied. Final Price: 499.99 TRY

Exactly 500

500.00

10

2

y

Order Approved: 10% member discount applied. Final Price: 450.00 TRY

Above 500

500.01

10

2

y

Order Approved: 10% member discount applied. Final Price: 450.01 TRY

Testing Notes

One test I ran: I tested an edge case where a user might enter a negative number or zero for the requested quantity (e.g., requested quantity = 0).

One thing I changed after testing: Initially, I only checked if the requested quantity was greater than the available stock. After testing, I added an if requested_quantity <= 0 condition at the very beginning to ensure invalid quantities are immediately rejected before any other logic runs.
