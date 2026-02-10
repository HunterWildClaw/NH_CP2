# NH 2nd Move recommender
#import csv
import csv

#Welcome the user
print("Welcome to my movie recommender!")

# read the movie list
def read_movies():
    with open("individual_projects\\movies_list.csv", "r") as movies:
        reader=csv.reader(movies)
        header=next(reader)
        movies=[]
        for line in reader:
            movies.append(
                {
                    header[0]: line[0].strip(),
                    header[1]: line[1].strip(),
                    header[2]: line[2].strip(),
                    header[3]: line[3].strip(),
                    header[4]: int(line[4].strip()),
                    header[5]: line[5].strip()
                }
            )
        
        return movies

#make main function
def main():
    movies=read_movies()
    #while loop it
    while True:
        #Give them their options
        user_choice = input("Here are your options:\nWould you like to\n1. Search for a movie\n2. Get a recommendation\n3. See whole list\n4. Leave\nWhat would you like to do?: ")
        #If they choose 1
        if user_choice=='1':
            #initiate the search function
            search(movies)
        #if user chose 2
        elif user_choice=='2':
            #initiate the recommender function
            recommendation(movies)
        # If user chose three
        elif user_choice=='3':
            #activate list function
            movie_list(movies)
            #If they chose 4 then leave the loop
        elif user_choice=='4':
            print("Byeeeeeeeeeeee!")
            break


#def search function
def search(movies):
    #Get user input
    search=input("Give title, genre, actors, or movie director: ")
    for i in movies:
        if search in movies:
            print(i)


#Def recommender function
def recommendation(movies):
    print("sup")


# Def movie lister function
def movie_list(movies):
    for i in movies:
        print(i)
main()