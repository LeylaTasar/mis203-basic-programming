while True:
    starting_balance = float(input("Starting balance: "))
    monthly_deposit = float(input("Monthly deposit: "))
    interest_rate = float(input("Monthly interest rate (%): "))
    goal = float(input("Savings goal: "))

    if starting_balance < 0 or interest_rate < 0 or monthly_deposit <= 0 or goal <= 0:
        print("Invalid input! Starting balance and interest rate cannot be negative. Deposit and goal must be positive. Please try again.")
    else:
        break

balance = starting_balance
total_interest = 0.0
months = 0

if balance >= goal:
    print("\nYour starting balance already meets the goal!")
    print(f"Goal reached: Yes, in 0 months")
    print(f"Final balance: {balance:.2f}")
    print(f"Total interest earned: {total_interest:.2f}")
else:
    print("\nMonth | Interest Earned | New Balance")
    print("-" * 37)

    while months < 60:
        months += 1

        interest_earned = balance * (interest_rate / 100)
        total_interest += interest_earned
        balance += interest_earned + monthly_deposit

        print(f"{months:<5} | {interest_earned:<15.2f} | {balance:.2f}")

        if balance >= goal:
            break

    print("-" * 37)

    if balance >= goal:
        print(f"Goal reached in {months} months.")
    else:
        print(f"Goal not reached: stopped after 60 months.")
        
    print(f"Final balance: {balance:.2f}")
    print(f"Total interest earned: {total_interest:.2f}")
