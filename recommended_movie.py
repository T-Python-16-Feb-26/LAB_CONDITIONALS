movie_name="6ash ma 6ash"

movie_rate=int(3)

popularity=float(72.65)

if 5>=movie_rate>=0:
    if movie_rate>=4 and popularity>80:
        print("Highly recommended")

    elif movie_rate>=3 and popularity>70:
        print("I recommended it. it is good")

    elif movie_rate<=2 and popularity>60:
        print("You should check it out")

    elif movie_rate<=2 and popularity<50:
        print("Don't watch it. It is waste of time")

else:
    print("invalid, insert number between 0 and 5")
        
