'''
Bonus 1
write a program that Calculates the BMI (body mass index) of the user:

    Ask the user to provide his wieght.
    Ask the user to provide hi height.
    print the BMI for the user.
    using conditionals tell the user that either :
        You are overwieght you need to work out more and watch your diet.
        You are fit & healthy.
        You are underweight. Watch your health.

Note

for formula , search the web.
BMI: weight / height^2
'''

print("###this is a bmi calculation program### \n")

weight = float(input("provide your weight(in kilograms): "))
height = float(input("provide your height(in meters): "))

print("your Bmi score is: ", weight/(height**2))
bmi_score = weight/(height**2)

if bmi_score >= 25:
    print("you are over weight you need to work more and watch your diet")
elif bmi_score >= 18.5 and bmi_score < 25:
    print("you are fit & healthy")
elif bmi_score < 18.5:
    print("you are underweight. Watch your health.")