print("Week 01 Exam - Combined Bill, Tip, and BMI CLI App")

total_bill = float(input("Enter total bill amount: "))
tip_percent = int(input("Enter tip percentage: "))
people_count = int(input("Enter number of people: "))

tip_amount = total_bill * tip_percent / 100
final_bill = total_bill + tip_amount
per_person = final_bill / people_count

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)
rounded_bmi = round(bmi, 2)

if bmi < 18.5:
    bmi_category = "underweight"
elif bmi < 25:
    bmi_category = "normal weight"
elif bmi < 30:
    bmi_category = "overweight"
else:
    bmi_category = "obese"

print(f"Final bill with tip: {final_bill:.2f}")
print(f"Each person pays: {per_person:.2f}")
print(f"BMI: {rounded_bmi} ({bmi_category})")
