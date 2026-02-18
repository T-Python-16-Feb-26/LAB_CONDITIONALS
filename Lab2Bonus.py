wieght:int = input("Enter your weight in kg: ")
height:float = input("Enter your height in meters: ")
bmi:float = int(wieght) / (float(height) * float(height))

print("Your BMI is: ", bmi)

if bmi >= 25:
    print("You are Overweight you need to work out more and watch your diet.")
elif bmi >= 18.5 and bmi < 25:
    print("You are fit & healthy.")
elif bmi < 18.5:
    print("You are Underweight. Watch your health.")
