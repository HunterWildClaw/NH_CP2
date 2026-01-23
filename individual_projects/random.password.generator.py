# NH 2nd Random Password Generator

def main():
    print("Hello and welcome to my Random Password Generator!")
    user_first_choice=input("Would you like to get generating or did you make a mistake and want to leave? Select '1' to start generating a password or '2' to leave ")
    if user_first_choice == '1':
        password_length=int(input("Great! Now how long would like your password to be?"))
        password_lower=int(input("Does it need lowercase letters? 1 for yes and 2 for no"))
        password_upper=int(input("Does it need uppercase letters? 1 for yes and 2 for no"))
        password_number=int(input("Does it need numbers? 1 for yes and 2 for no"))
        password_special_char=int(input("Do you want special characters? 1 for yes and 2 for no"))
        print("Here are the available passwords:")



main()