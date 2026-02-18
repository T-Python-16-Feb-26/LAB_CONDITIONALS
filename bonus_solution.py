
user_wieght= float(input("Please enter your wieght in kilograms: "))
user_height=float(input("Please enter your height in meters: "))

BMI= user_wieght/ (user_height**2)

print("Your BMI is:",round(BMI,3))


if BMI >= 25:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI >= 18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")

