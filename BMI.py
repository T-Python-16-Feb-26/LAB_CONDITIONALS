wieght = float(input("what is your wieght (kg):"))
height =float(input("what is your height(m):"))
BMI = wieght / (height ** 2)
print(f" your BMI is:{BMI}")
if BMI >= 25 :
    print(" you are overwieght you need to work out of more and watch your diet")
elif BMI >= 19 :
    print(" you are fit and healthy")
else:
    print("you are underweight watch your health")
