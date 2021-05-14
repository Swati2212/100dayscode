weight = int(input("Enter your weight in kg? "))
height = float(input("Enter your height in m? "))

bmi = round(weight / (height * height))

if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
