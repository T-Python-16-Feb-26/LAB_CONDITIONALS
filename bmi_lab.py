weight = float(input("Enter your weigh: "))       # in kilograms
height = float(input("Enter your height: "))    # in meters

# Calculate BMI
bmi = weight / (height * height)
print("Your Body Mass Index (BMI) = ", round(bmi, 2))

# Determine BMI category
if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif bmi >= 18.5 and bmi < 25:
    print("You are fit & healthy.")
else:
    print("You are overweight. You need to work out more and watch your diet.")