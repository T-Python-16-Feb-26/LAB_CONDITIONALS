weight:str= input("Enter your Weight : ")
height:str= input("Enter your height : ")
weight=float(weight)
height=float(height)
BMI= round(weight / height**2,2)
if BMI >= 25:
    print("The BMI is : ",BMI,"\nYou are overwieght you need to work out more and watch your diet")
elif BMI >=18.5:
    print("The BMI is : ",BMI,"\nYou are fit & healthy")
else:
    print("The BMI is : ",BMI,"\nYou are underweight. Watch your health")