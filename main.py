movie:str = "intersteller"
rate:int = 3
popularity:float = 72.65

if rate >= 4 and popularity > 80:
    print("Highly recommended")
elif rate >= 3 and popularity > 70:
    print("I recommended it. It is good")
elif rate <= 2 and popularity > 60:
    print("You should check it out")
else:
    print("watch it. it is a waste of time")
    