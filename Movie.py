Movie:str = "blacklist"

rating:int = 3
score:float = 72.65
if rating >= 4 or score >= 80.0:
    print("Highly recommended")
elif rating >= 3 and score >= 70.0:
    print("I recommend it . It is good")
elif rating >= 2 and score >= 60.0:
    print("you shuld check it out!")
else:
    print("Don't watch it. It is a waste of time")

