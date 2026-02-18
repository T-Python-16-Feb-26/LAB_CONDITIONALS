
wieght = float(input("your wieght : "))
height = float(input("your height : "))

BMI = wieght / (height**2)
print (BMI)

if BMI >=30:
    print('You are overwieght you need to work out more and watch your diet.')
elif BMI >=18:
    print('You are fit & healthy.')
else :
    print('You are underweight. Watch your health.')
