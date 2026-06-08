print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill? "))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

tip_amount = total_bill * tip_percent / 100
final_bill = total_bill + tip_amount
bill_per_person = final_bill / people_count

print(f"Each person should pay: {bill_per_person:.2f}")
