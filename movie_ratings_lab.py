#Define the variables for the movie name, rating, and popularity score
movieName = "Inception"
movieRating:int = 3
popularityScore:float =  72.65

#Start the conditional statement
if movieRating >=4 and popularityScore > 80:
    print("Highly recommended")
elif  movieRating >=3 and popularityScore > 70:
    print("I recommended it . It is good")
elif  movieRating >=2 and popularityScore > 60:
    print("You should check it out!")
elif movieRating <= 2 and popularityScore < 50:
    print("Don't watch it. It is a waste of time")