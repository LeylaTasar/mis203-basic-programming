# Lab 05: Shipping Quote

## Print vs. Return
- **`return`**: Passes a value back to the program. The program can store this value in a variable and use it for further calculations (e.g., using the returned discount rate to calculate the final total).
- **`print`**: Only outputs text to the terminal screen for the user to read. It does not store or pass any data back to the program, meaning you cannot use a printed value in mathematical operations.

## Development Notes
- **Test Ran:** Tested if the 10% discount applies at the exact boundary value of 100 using `assert get_discount_rate(100.0) == 0.10`.
- **Change Made:** Simplified the code in the `calculate_final_total` function by moving the discount calculation directly into the `return` statement instead of using a separate variable.
