print("welcome in Movie rating system\n")
Movie:str="Movie"
MovieRating:int =3
MovieScore:float=72.65



if MovieRating >=4 and MovieScore >80:
    print("Highly recommended")
elif MovieRating >=3 and MovieScore >70:
    print("I recommended it . It is good")
elif MovieRating <=2 and MovieScore >60 :
    print("You should check it out!")
elif MovieRating <=2 and MovieScore <50 :
    print("Don't watch it. It is a waste of time")
else:    
    print("It is an average movie")