print("welcome in BMI calculator\n")

weight=float(input("Enter your weight : "))
heightCm=float(input("Enter your height in CM : "))

height=heightCm/100

BMI= round(weight/(height * height), 2)
print("Your BMI is : ", BMI)


if BMI <18:
    print("Your weight is less than normal ,you should see a doctor ")
elif BMI >=18 and BMI <25:
    print("Your weight is normal")
elif BMI >=25 and BMI <30:
    print("Your weight is more than normal")
else  :
    print("Your weight is obese,you should see a doctor")