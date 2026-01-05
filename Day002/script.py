# Day 2: Tip Calculator
print("Welcome to the Tip Calculator! 💸")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? (10, 12, or 15): "))
people_count = int(input("How many people to split the bill? "))

# --- CALCULATION SECTION ---

tip_amount = total_bill * (tip_percentage / 100)
total_to_pay = total_bill + tip_amount
amount_per_person = total_to_pay / people_count
final_amount = "{:.2f}".format(amount_per_person)
print(f"Each person should pay: ${final_amount}")