# NH 2nd Move recommender
#import csv
import csv

#Welcome the user
print("Welcome to my movie recommender!")

#make main function
def main(movies):
    #while loop it
    while True:
        #Give them their options
        user_choice = input("Here are your options:\nWould you like to\n1. Search for a movie\n2. Get a recommendation\n3. See whole list\n4. Leave\nWhat would you like to do?: ")
        if user_choice=='1':
            search(movies)
        elif user_choice=='2':
            recommendation(movies)
        elif user_choice=='3':
            movie_list(movies)
        elif user_choice=='4':
            print("Byeeeeeeeeeeee!")
            break