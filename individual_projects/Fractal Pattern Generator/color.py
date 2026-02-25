#NH 2nd Fractal Pattern Generator color changer
#Import turtle
import turtle as t
#Make the color function
def color():
    #ask user what color they want for their Sierpinski Triangle 
    color = input("What color would you like your triangle to be? (Red. Orange, Yellow, Green, Blue, Teal, Purple, Pink, or just Black)\nEnter here: ").title().strip()

    #Depending on the color they chose, change the color to that color
    if color == "Red":
        t.color("red")

    elif color == "Orange":
        t.color("orange")

    elif color == "Yellow":
        t.color("yellow")

    elif color == "Green":
        t.color("green")

    elif color == "Blue":
        t.color("blue")

    elif color == "Teal":
        t.color("teal")

    elif color == "Purple":
        t.color("purple")

    elif color == "Pink":
        t.color("pink")

t.done()