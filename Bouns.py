# Bouns - write a program that Calculates the BMI (body mass index) of the user

print("Hi, I am your simple BMI Calculator! Please provide your information.\n")

#User Input 
user_weight: float = float(input("Enter your weight in kg: "))
user_height: float = float(input("Enter your height in cm: "))
user_age: int = int(input("Enter your age: "))
user_gender: str = input("Enter your gender (M/F): ")


# BMI Calculation

user_height_m = user_height / 100

BMI: float = user_weight / (user_height_m ** 2)

# Program Output

print(f"\nWeight: {user_weight:.2f} kg")
print(f"Height: {user_height:.2f} cm")
print(f"Age: {user_age} years old")
print(f"Gender: {user_gender}")
print(f"Your BMI is: {BMI:.2f}\n")

# BMI Classification

if BMI < 18.5:
    print("You are underweight. Watch your health.")

elif 18.5 <= BMI < 24.9:
    print("You are fit & healthy.")

elif 25 <= BMI < 30:
    print("You are overweight. You need to work out more and watch your diet.")

elif BMI > 30 :
    print("You are obese. You need to work out more and watch your diet.")




