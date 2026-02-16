#Nh 2nd pers lib update
import csv
import os

# your personal library file
db_file = "library.csv"
# these are the columns for your csv
headers = ['Title', 'Author', 'Year', 'Pages']

# load books from csv as dictionaries
def load_library():
    shelf = []
    if os.path.exists(db_file):
        with open(db_file, 'r', newline='') as file:
            # reader uses the first row as keys!
            reader = csv.DictReader(file)
            for row in reader:
                shelf.append(row)
    return shelf

# save the list of dictionaries back to the csv
def save_library(shelf):
    with open(db_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader() # writes title, author, etc. at the top
        writer.writerows(shelf)

# initialize our library
books = load_library()

# helper function for input
def input_helper(prompt='> '):
    # take user input and return it
    return input(prompt).strip().lower()

# search function - now checks all categories
def search(shelf):
    # have them give book details
    query = input_helper("Input search term (title, author, or year): ") 
    maybe = []
    # loop over books
    for book in shelf:
        # checks if query is in any of the book's details
        if any(query in str(value).lower() for value in book.values()):
            maybe.append(book)
    # return potential books
    return maybe

# show books function - formatted for columns
def show_books(shelf):
    if not shelf:
        print("Your shelf is empty! Go add some books!")
        return
    # display the header row
    print(f"{'#':<3} {'Title':<20} {'Author':<15} {'Year':<6} {'Pages'}")
    print("-" * 55)
    for i, book in enumerate(shelf, 1):
        # show the book formatted nicely
        print(f"{i:<3} {book['Title']:<20} {book['Author']:<15} {book['Year']:<6} {book['Pages']}")

# upgraded add book function
def add_book():
    # get the details
    name = input_helper("What's the title of your new book?: ").title()
    author = input_helper("And who's the author?: ").title()
    year = input_helper("Year published: ")
    pages = input_helper("Number of pages: ")
    
    # show that you've added the book
    print(f"Sweet! I've added {name} by {author} ({year})")
    
    # now make it a dictionary matching our headers
    return {
        'Title': name,
        'Author': author,
        'Year': year,
        'Pages': pages
    }

# select book function
def select(options):
    # display book options numbered
    if not options:
        print("Nothing found to select!")
        return False
    show_books(options)
    while True:
        # take user input
        choice = input_helper('Choose book (by number) or 0 to exit: ')
        # if choice is 0:
        if choice == '0':
            return False
        # if choice is a number
        try:
            return options[int(choice)-1]
        # otherwise:
        except:
            print('Please choose by number! Not the actual title!')
            continue

# main library function
def lib():
    global books
    while True:
        # display choices
        print("Welcome to your Library! Options: \n1. Add\n2. View\n3. Remove\n4. Search\n5. Exit")
        
        # take user input for one of the choices
        while True:
            choice = input_helper()
            if choice in ['1', 'add', '2', 'view', '3', 'remove', '4', 'search', '5', 'exit']:
                break
            else:
                print('QUIT TROLLING!!!!\nPlease select one of the choices!')

        # if choice is add
        if choice in ['1', 'add']:
            books.append(add_book())
            save_library(books)
            
        # if choice is view
        elif choice in ['2', 'view']:
            show_books(books)
            
        # if choice is remove
        elif choice in ['3', 'remove']:
            # book search
            potential = search(books)
            # chosen = book select
            chosen = select(potential)
            if chosen:
                # remove chosen from list
                books.remove(chosen)
                save_library(books)
                print(f"Removed {chosen['Title']}")
            else:
                print('\033c')
                continue
                
        # if choice is search
        elif choice in ['4', 'search']:
            searched = search(books)
            show_books(searched)
            
        # if choice is exit
        elif choice in ['5', 'exit']:
            # tell the user goodbye
            print('\033ccya!')
            return
            
        # return to top of function
        input('\nPress Enter to continue')
        print('\033c')

# start the thing!
lib()