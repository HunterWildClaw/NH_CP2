#NH 2nd Personal Library
#Create a set for the books

books = set({})
#make a ui function as the helper function
def input_helper(prompt = '> '):
    #take user input and return it
    return input(prompt).strip().lower()

#make the add book function
def add_book():
    #get the name
    name = input_helper("What's the title of your new book?: ")
    #then the author
    author = input_helper("And who's the author?: ")
    #then show that youve added the book
    print(f"Sweet! I've added {name.title()} by {author.title()}")
    #now make it a dictionary
    book = f'{name.title()} by {author.title()}'
    #then return the book
    return book

#show books function
def show_books(shelf):
    #loop over all the books
    i = 0
    for book in shelf:
        i += 1
        #show the book
        print(f'{i}. {book}')

#make a search function
def search(shelf):
    #have them give book title or author
    search = input_helper("Input name of book or author: ") #Yes i said input get over it  
    #create list for potential books
    maybe = []
    #loop over books
    for book in shelf:
        #if current book title contains query:
        if search in book.lower():
            #add current book to potential books
            maybe.append(book)
    #return potential books
    return maybe

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
            print('Please choose by number! Not the actual title!')
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
        input('Press Enter to continue')
        print('\033c')
lib()