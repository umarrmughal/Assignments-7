#exercise 4
'''. Movie Recommendation System: Create a program that recommends movies based on user 
preferences. Use variables to store genre, rating, and release year. Write expressions to 
compare movies and suggest matches.'''

#program
movies = [
    {'title':"The dark knight",'genre':'action','rating':9.0,'release_year':2008},
    {'title':'the lord of the rings','genre':'adventure','rating':8.9,'release_year':2003},
    {'title':'pulp fiction','genre':'comedy','rating':8.9,'release_year':1994},
    {'title':'the shawshank redemption','genre':'drama','rating':9.3,'release_year':1994},
    {'title':"the shining",'genre':'horror','rating':8.4,'release':1980}
]


user_genre = input("Enter genre:")
user_rating = float(input("Enter rating:"))



recommended_movie = []

for movie in movies:
    if movie['genre'] == user_genre and movie['rating'] >= user_rating:
        recommended_movie.append(movie['title'])




if recommended_movie:
    print("Recommended movie:")
    for movie in recommended_movie:
        print(movie)
else:
    print("No movives found matching your prefrences.")