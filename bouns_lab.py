

# BMI = weight (kg) / height² (m)

weight = int(input("Enter your wieght : "))
height = int(input("Enter your height : "))



convert_height_cm_to_meter = height/100
bmi_formula = weight//(convert_height_cm_to_meter**2)


if bmi_formula >= 25 and height >= 110:
    print("your bmi is:", bmi_formula, "You're overwieght. You need to watch your diet and workout more.")

elif 18 <= bmi_formula <= 24 and height >= 110:
    print("your bmi is:", bmi_formula, "You are fit & healthy.")

elif bmi_formula <= 18 and height >= 110 :
    print("your bmi is:", bmi_formula, "You are underweight. Watch your health.") 
else:
    print("invalid")    
