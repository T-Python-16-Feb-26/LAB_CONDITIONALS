print("#"*30)
print("\nLets see what your BMI is\n")
print("#"*30)
weight = float(input("What's your weight in kg? "))
height = float(input("What's your height in cm? "))

bmi = weight / (height/100)**2
print(f"Your BMI is {bmi:.2f}")
if bmi >= 25:
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi >= 18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")