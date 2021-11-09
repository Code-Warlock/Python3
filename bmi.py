weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meters : "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("You're Underweight. Eat more.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Healthy Weight.You're eating well.")
elif bmi >= 25.0 and bmi <= 29.9:
    print("You're overweight....Just drink gaari for 1 yr.")
else:
    print("Obese.Don't eat for 2 years.")
