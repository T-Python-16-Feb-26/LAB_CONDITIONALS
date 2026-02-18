movie:str = "paddington"
rate:int = 3
popularityScore:float = 72.65

if rate>=4 and popularityScore>80:
    print("Highly recommended")
elif rate >=3 and popularityScore>70:
    print ("I recommended it. it is good")
elif rate <=2 and popularityScore>60:
    print("you should check it out!")
else:
    print ("dont watch it, it is a waste of time")