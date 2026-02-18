weight:float = float(input("Enter Your weight in kg: "))
height:float = float(input("Enter Your height in cm: ")) / 100

BMI:float = weight / (height**2)
print(f"Your BMI: {round(BMI,2)}")
if BMI >= 25.0:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")