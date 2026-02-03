#NH 2nd morse code thing
import time

# make the tuples for English and morse characters
english_letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ')

morse_letters = ('.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', 
                 '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '/')

# make the function for eng to morse
def english_to_morse(code):
    morse_msg = []
    for char in code.upper():
        if char in english_letters:
            index = english_letters.index(char)
            morse_msg.append(morse_letters[index])
    return " ".join(morse_msg)

# now the function for morse to english
def morse_to_english(code):
    english_msg = []
    # Morse characters are separated by spaces
    words = code.split(" ")
    for code in words:
        if code in morse_letters:
            index = morse_letters.index(code)
            english_msg.append(english_letters[index])
    return "".join(english_msg)

    # def main menu 
def main_menu():
    # infinite loop it
    while True:
        print("\nWelcome to morse code generator!\nYour options are:")
        print("1) English to Morse")
        print("2) Morse to English")
        print("3) Quit")
        
        choice = input("Select an option (by number): ")
        
        if choice == '1':
            msg = input("Enter your message to encode: ")
            print("\nHere ya go!:", english_to_morse(msg))
            time.sleep(.9)
        elif choice == '2':
            msg = input("Enter your message to uncode: ")
            print("\nHere ya go!:", morse_to_english(msg))
            time.sleep(1)
        elif choice == '3':
            print("K cya!")
            break
        else:
            print("Invalid input, try again.")

main_menu()