
weight:float = float(input("Enter your weight in kg: "))
height:float = float(input("Enter your height in meters: "))

bmi:float = weight / (height * height)

print(f"Your BMI is: {bmi:.2f}")

if bmi >= 25:
    print("You are overweight you need to work out more and watch your diet")
elif bmi >= 18.5 and bmi < 25:
    print("You are fit & healthy")
else:
    print("You are underweight. Watch your health")
