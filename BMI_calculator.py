weight=float(input("insert your weight: "))

height=float(input("insert your height: "))

BMI=(weight/((height/100)**2))

print(f"Your BMI is {BMI:.1f}")

if BMI <18.5:
    print("Underweighted. watch your health")

elif 24.9>=BMI>=18.5:
    print("You are fit & healthy")

else:
    print("You are overweight you need to work out more and watch your diet")


