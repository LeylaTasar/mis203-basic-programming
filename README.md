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



## Week 03

**AI Tool Used:** Gemini
**Prompt Used:** "Your program sells cinema tickets. It keeps running until the user wants to stop. Ask for the customer name... [I provided the exact assignment prompt constraints, discounts, and expected output block]"
**What did you change?:** I placed the main logic inside a `while True` loop and used `continue` statements to reset the loop anytime invalid inputs (age outside 0-120, invalid day, or invalid student response) are detected. I also set up an `if-elif-else` chain that checks the age limits and student status sequentially to apply the single most appropriate discount. 
**Tests:** 
1. **Input:** Name: Can, Age: 5, Day: weekend, Student: no -> **Result:** Can: 0.00 TRY (Free)
2. **Input:** Name: Zeynep, Age: 20, Day: Weekday, Student: yes -> **Result:** Zeynep: 140.00 TRY (Student)
3. **Boundary Test:** Name: Ali, Age: 25, Day: weekday, Student: yes -> **Result:** Ali: 140.00 TRY (Student) (Tested the exact boundary age of 25 for the student limit)
**Why does the order of the rules matter?:** The order matters because an `if-elif` statement stops checking as soon as it finds a match. If the "Student" rule was checked before the "Child" rule, a 10-year-old student would trigger the 30% Student discount and the program would skip over the 40% Child discount, causing them to pay more than they should.


  
