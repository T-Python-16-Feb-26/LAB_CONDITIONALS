# Define the variables by user input
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Calculate BMI
bmiCalculates = (weight / (height ** 2))
print(f"Your body mass index is: {bmiCalculates:.2f}")

# Conditional statement to classify BMI
if bmiCalculates < 18.5:
    print("You are underweight. Watch your health.")
elif 18.5 <= bmiCalculates < 25:
    print("You are fit & healthy.")
elif 25 <= bmiCalculates < 30:
    print("You are overweight. Try to exercise more and watch your diet.")

print("Stay healthy and take care of yourself!")