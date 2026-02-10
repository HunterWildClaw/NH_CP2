# NH 2nd Movie recommender
#import csv
import csv

# def read movies function
def load_movies(filename):
    #Make the movies variable
    movies = []
    #Try and accept
    try:
        with open("individual_projects/movies.csv", 'r') as file:
            # DictReader uses the first row of your CSV as keys for each movie dictionary (I looked it up ;)
            reader = csv.DictReader(file)
            #for every row in the file:
            for row in reader:
                #add it to the movies variable
                movies.append(row)
            #If I messed up and the file don't exist:
    except FileNotFoundError:
        #Tell the user that the program failed :(
        print(f"{filename} not found.")
    #return movies
    return movies

# def search function
def search(movies):
    #Make the search query
    query = input("Give title, genre, actors, or movie director: ").lower()
    #Set it to false
    found = False
    print("\nSearch Results\n")
    for movie in movies:
        # check every value in the movie's dictionary (title, genre, etc.)
        if any(query in str(value).lower() for value in movie.values()):
            print(f"Title: {movie.get('Title')} | Genre: {movie.get('Genre')}")
            found = True
    if not found:
        print("No matching movies found.")

# def movie recommender
def recommendation(movies):
    #Ask what genre they want
    genre_choice = input("What genre do you like? (e.g., Action, Comedy): ").lower()
    print(f"\nRecommended {genre_choice.capitalize()} Movies")
    count = 0
    for movie in movies:
        # Checks if the user's genre is inside the 'genres' column
        if genre_choice in movie.get('Genre', '').lower():
            print(f"- {movie.get('Title')}")
            count += 1
            if count >= 5: # Limit recommendations to 5 to avoid flooding
                break
    if count == 0:
        print("Sorry, no movies found in that genre.")

# def movie list function
def movie_list(movies):
    print("\nFull Movie List")
    for movie in movies:
        print(f"{movie.get('Title')} ({movie.get('Genre')})")
    print("Sry bout da flood.")

# def main function
def main(movies):
    while True:
        print("\nMain Menu:\nWould you like to:")
        user_choice = input("1. Search for a movie\n2. Get a recommendation\n3. See whole list\n4. Leave\nWhat would you like to do?: ")
        
        if user_choice == '1':
            search(movies)
        elif user_choice == '2':
            recommendation(movies)
        elif user_choice == '3':
            movie_list(movies)
        elif user_choice == '4':
            print("Byeeeeeeeeeeee!")
            break
        else:
            print("Invalid choice, try again.")

# start the program
movie_data = load_movies('movies.csv')
if movie_data:
    main(movie_data)
