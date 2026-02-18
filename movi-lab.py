# chosen movie
movie = "Inception"

# rating out of 5 (int)
rating = 3

# popularity score (float)
popularity = 72.65

# decision logic
if rating >= 4 and popularity > 80:
    print("Highly recommended")
elif rating >= 3 and popularity > 70:
    print("I recommended it . It is good")
elif rating <= 2 and popularity > 60:
    print("You should check it out!")
else:  # rating <= 2 and popularity < 50
    print("Don't watch it. It is a waste of time")

