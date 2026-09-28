# mis203-basic-programming

##Week 01

Name: [Leyla Taşar]
Student Number: [2404109010]
Department: [Management Information Systems]
Course Name: MIS203 Basic Programming

AI Tool Used: Google Gemini
Prompt Used: Create a simple Python program that asks the user for their Name, Department, Age, and Career Goal, and then prints a short student profile.
What did you change?: I used the code directly but reviewed the input functions and variables to ensure I understand how they capture and display data.


## Week 02

AI Tool Used: Gemini

Prompt Used: Create a folder named: week02 Write a Python program named: grade_calculator.py... 

What did you change?
I reviewed the provided code to ensure the `if-elif` logic for letter grades matched the requested ranges. I also added a check (`is_integer()`) so that whole numbers print cleanly (like 85 instead of 85.0).

What does break do in your program?
The `break` statement immediately stops the infinite `while True` loop as soon as the user enters 'q', allowing the program to exit the loop and print the final average score.



# Week 1 Lab Quiz Notes

### Test & Modification
* **Test Run:** I tested the program by entering standard student details and also tested an empty string for the name field (boundary case).
* **Change Made After Testing:** I added alignment spaces and border lines (`====`) to make the card heading and output cleaner and more readable.

### Acceptance Check #4 Explanation
* **`input()`:** Captures user keyboard entry and stores the data as a string (`str`) inside a variable.
* **`print()`:** Displays the formatted string output on the terminal screen.

### Stretch Task
* **Empty Name Behavior:** When an empty name is entered (pressing Enter directly), the program stores an empty string `""` and leaves the Name field blank without crashing.
* **Future Improvement:** In the future, we can add a `while` loop or `if` condition to validate that the name is not empty before printing the card.


# Week 02 Lab Quiz - Two-Item Purchase Quote

## Test Runs
* **Standard Test Case:** Tested with Item 1 (`quantity = 2`, `unit price = 50`), Item 2 (`quantity = 1`, `unit price = 80`), `delivery fee = 20`, and `tax = 10%`. The program calculated a subtotal of `180.00 TRY`, tax of `18.00 TRY`, and the expected final total of `218.00 TRY`.
* **Boundary / Error Case (Stretch Task):** Tested entering letters (`abc`) instead of a number for the quantity input. The program stopped with the following error message:
  `ValueError: invalid literal for int() with base 10: 'abc'`
  * **How a later version could handle it:** A future version could use a `try-except ValueError` block inside a `while` loop (or check `.isdigit()`) to catch invalid inputs and prompt the user to enter a valid integer without crashing the program.

## What I Changed After Testing
* After running the initial test, I updated the output formatting using `:.2f` in the f-strings so that all monetary values (unit prices, line totals, subtotal, tax, delivery fee, and final total) consistently display with two decimal places.

## Why `input()` Must Be Converted Before Arithmetic
* In Python, the `input()` function always returns user input as a text string (`str`). If we do not convert it using `int()` or `float()` before arithmetic operations, the `+` operator will concatenate strings instead of adding numbers, and multiplication/division operations will fail with a `TypeError`.
  
