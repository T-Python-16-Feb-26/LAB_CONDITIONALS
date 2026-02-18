
print("Welcome to BMI calculator website!")
print("To complete the process. please enter your wieght:")
wieght = float(input())
print ("Nice! and now enter your height:")
height = float(input()) / 100

BMI = wieght /(height**2) 

if BMI >=40:
    print ("You are overwieht! you need to work out more and watch your diet!")
elif BMI<40 and BMI>=35:
    print ("you are grade 2 obesity")
elif BMI<35 and BMI>=30:
    print ("you are grade 1 obesity")
elif BMI <30 and BMI>=25:
    print ("you are fat")
elif BMI <25 and BMI>=18:
    print ("You are normal. fit & healthy")
else: 
    print("you are underweight. watch your health")