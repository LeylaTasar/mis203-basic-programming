# Lab 04 - Savings Goal Planner

## Test Run
I tested the program using the parameters from the second acceptance check:
* **Starting balance:** 1000
* **Monthly deposit:** 500
* **Monthly interest rate:** 1%
* **Savings goal:** 3000

**Result:** The program successfully stopped after 4 months. It printed a final balance of `3070.80` and a total interest of `70.80`, which perfectly matched the expected output in the instructions.

## Change After Testing
During my initial testing, my final balance was slightly off. I realized that my while loop was adding the monthly deposit to the balance *before* calculating the monthly interest. I updated the code to calculate and add the interest based on the current balance first, and then add the monthly deposit, which fixed the mathematical error.
