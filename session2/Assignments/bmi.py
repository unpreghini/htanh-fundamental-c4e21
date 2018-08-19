height_cm = int(input("Please enter your height in cm: "))
weight = int(input("Please enter your weight in kg: "))

height = height_cm / 100

BMI = weight / (height*height)
print("Your Body Mass Index (BMI) = ", BMI)

if BMI < 16:
    print("BMI indicates you are Severly Underweight")

elif BMI < 18.5:
    print("BMI indicates you are Underweight")

elif BMI < 25:
    print("BMI indicates you are Normal")

elif BMI < 30:
    print("BMI indicates you are Overweight")

else:
    print("BMI indicates you are Obese")
