# Task1: You want to recommend a movie to a friend based on the rating and popularity . To accomplish this do the following :


movie_name: str = "Harry Potter"
rate:int = 3
popularity_score:float = 72.65

print (f"Movie Name: {movie_name}")
print(f"Movie Rate: {rate} out of 5")
print(f"Popularity Score: {popularity_score:.2f}")
print()


if rate >= 4 and popularity_score > 80:
    print("Highly recommended")

elif rate >= 3 and popularity_score > 70:
    print("I recommend it. It is good")

elif rate >= 2 and popularity_score > 60:
    print("You should check it out!")

else:
    print("Don't watch it. It is a waste of time")





