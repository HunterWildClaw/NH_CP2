# NH 2nd Financial Calulator
#Import math cuz yes
import math

#Ask user if they wanna do Compound Interest Calculator, Budget Allocator, Sale Price Calculaton, or Tip Calculator
def financial_calc():
    user_choice=input("Would you like to use the \n1) Compound Interest Calculator \n2) Budget Allocator\n3) Sale Price Calculaton\n4)Savings Time Claculator\n5) Tip Calculator\nEnter number here: ").strip()
    #If user trolled
    #if the user picked 1:
    if user_choice=='1':
        starting_ammount=int(input("What's your starting ammount?: "))
        interest_rate_percent=int(input("And what's the interest rate percent?: "))
        years_spent_compounding=int(input("And finally, how many years will you spend compunding?: "))
        for i in years_spent_compounding:
            new_amount=starting_ammount*(interest_rate_percent/100+1)
        print(f"After {years_spent_compounding}, with an interest rate of {interest_rate_percent}, your starting ammount of ${starting_ammount} will become ${new_amount}!")
        
financial_calc()