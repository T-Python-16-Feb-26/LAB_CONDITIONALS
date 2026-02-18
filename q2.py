wieght=float(input("please enter your wieght in kg :"))
height=float(input("please enter your height cm :"))
height=height/100

Bmi=wieght/(height**2)

print(f"Your BMI is:{Bmi:.2f}")

if Bmi>=25:
    print("You are overweight you need to work out more and watch your diet.")
elif Bmi>=18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")












