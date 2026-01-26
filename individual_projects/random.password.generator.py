# NH 2nd Random Password Generator
#import random as r
import random as r

#Make the things that hold all the characters
caps_letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters= "abcdefghijklmnopqrstuvwxyz"
nums=[1,2,3,4,5,6,7,8,9]
special_chars="!@#$%^&*()¡™£¢∞§¶•ªº⁄€‹›ﬁﬂ‡°·‚œ∑´®†¥¨ˆøπåß∂ƒ¬…“‘«÷≥≤µ˜∫√ç≈ΩŒ„´‰ˇÁ¨ˆØ∏”’ÅÍÍÎÏ˝ÓÔÒÚÆ»`¸˛Ç◊ı˜Â¯˘¿Ω=-+_≠–±—"

def get_input(prompt):
    while True:
        answer=input(prompt)
        if answer == "1":
            return True
        if answer == "2":
            return False
        print("Invalid input. Try again")


def info_getter_and_password_generator():
    password_length=get_input("How long would you like your password to be? Please give a number: ").strip()
    password_lower=get_input("Does it need lowercase letters? '1' for yes and '2' for no: ").strip()
    password_upper=get_input("Does it need uppercase letters? '1' for yes and '2' for no: ").strip()
    password_number=get_input("Does the password need numbers? '1' for yes and '2' for no: ").strip()
    password_special_chars=get_input("Does the password need special characters? '1' for yes and '2' for no: ").strip()

def main():
    while True:
        print("Hello and welcome to my Random Password Generator!")
        user_first_choice=get_input("Would you like to make a password? '1' for yes and '2' for no: ")
        if user_first_choice=='1':
            info_getter_and_password_generator()
        

main()