



movie_name:str = "12 angry men"
movie_rating_IMDb:int = 3 #the rating is from 5. (3/5)
popularity_score:float = 72.65

print("-"*10)

print(movie_name)

if movie_rating_IMDb >= 4 and popularity_score >=80:
    print("Highly recommended")
elif movie_rating_IMDb >= 3 and popularity_score >=70:
    print("I recommended it . It is good")
elif movie_rating_IMDb >= 2 and popularity_score >= 60:
    print("You should check this out!")
else: 
    print("Don't watch it. It's a waste of time..")
        

