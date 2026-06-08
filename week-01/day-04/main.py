print("Welcome to the BMI Interpretation Calculator!")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)
rounded_bmi = round(bmi, 2)

if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal weight"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"

print(f"Your BMI is {rounded_bmi}, which means you are {category}.")
