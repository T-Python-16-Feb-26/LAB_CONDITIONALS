wieght:float = float(input("whats your wieght in kg:"))
hight:float = float(input("whats your hight in meter:"))
BMI = wieght/hight**2

if BMI >= 24.9:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI > 18.5 and BMI < 24.9:
    print("You are fit & healthy.")
elif BMI <= 18.5:
    print("You are underweight. Watch your health.")