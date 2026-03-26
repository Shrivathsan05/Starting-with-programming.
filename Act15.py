#Write a program to calculate the BMI of a person?
Height = float(input("Enter your Height in cm: "))
Weight = float(input("Enter your Weight in kg: "))

BMI = Weight / (Height/100)**2

print ("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight!")
elif BMI <= 24.9:
    print("You are healthy!")
elif BMI <= 29.9:
    print("You are overweight!")
elif BMI <= 34.9:
    print("You are severly overweight!")
elif BMI <= 39.9:
    print("You are obese!")
else:
    print("You are severly obese!")

