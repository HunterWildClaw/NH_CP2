#NH 2nd Personal Library
#Create set for books

books = set({})
#user input function
def input_helper(prompt = '> '):
    #take user input and return it
    return input(prompt).strip().lower()

#book input function
def add_book():
    #name = take user input "Title: "
    name = input_helper("What's the title of your new book?: ")
    #author = take user input "Author: "
    author = input_helper("And who's the author?: ")
    #display "Added (title) by (author)"
    print(f"Sweet! I've added {name.title()} by {author.title()}")
    #book = dictionary containing title: name and author: author
    book = f'{name.title()} by {author.title()}'
    #return book
    return book

#display books function
def show_books(shelf):
    #loop over books
    i = 0
    for book in shelf:
        i += 1
        #display "(current book title) by (current book author)"
        print(f'{i}. {book}')

#search books function
def search(shelf):
    #query = take user input "search"
    query = input_helper("Input name of book or author: ")
    #create list for potential books
    potential = []
    #loop over books
    for book in shelf:
        #if current book title contains query:
        if query in book.lower():
            #add current book to potential books
            potential.append(book)
    #return potential books
    return potential

#select book function
def select(options):
    #display book options numbered
    show_books(options)
    while True:
        #take user input "choose book (by number) or 0 to exit: "
        choice = input_helper('Choose book (by number) or 0 to exit: ')
        #if choice is 0:
        if choice == '0':
            #exit function
            return False
        #if choice is a number
        try:
            #return book with that number
            return options[int(choice)-1]
        #otherwise:
        except:
            #ask again
            print('Please choose by number!')
            continue

#main function
def lib():
    while True:
        #display choices
        print("Hello and welcome to your own personal library! Here are your options: \n1. Add\n2. View\n3. Remove\n4. Search\n5. Or Exit")
        #take user input for one of the choices
        while True:
            choice = input_helper()
            if choice in ['1','add','2','view','3','remove','4','search','5','exit']:
                break
            else:
                print('QUIT TROLLING!!!!\nPlease select one of the choices!')
        #if choice is add
        if choice in ['1','add']:
            #add (book input) to books
            books.add(add_book())
        #otherwise if choice is view
        elif choice in ['2','view']:
            #display books
            show_books(books)
        #otherwise if choice is remove
        elif choice in ['3','remove']:
            #book search
            potential = search(books)
            #chosen = book select
            chosen = select(potential)
            #if chosen is empty:
            if chosen == False:
                #return to top of function
                print('\033c')
                continue
            #remove (chosen) from books
            books.remove(chosen)
            print(f'Removed {chosen}')
        #otherwise if choice is search
        elif choice in ['4','search']:
            #book search
            searched = search(books)
            #display the books
            show_books(searched)
        #otherwise if choice is exit
        elif choice in ['5','exit']:
            #tell the user goodbye
            print('\033ccya!')
            #exit program
            return
        #return to top of function
        input('Press Enter to Continue: ')
        print('\033c')
lib()