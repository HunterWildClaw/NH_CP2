# NH 2nd Sierpinski Triangle (TRIFORCE!)
# Import the stuff
import turtle
from triangle import draw_sierpinski
from color import color_setter

def main():
    print("Welcome to my Sierpinski Triangle Generator!")
    # Set the settings
    t = turtle.Turtle()
    t.color(color_setter())  # Call the function to get the color
    t.hideturtle()
    t.penup()
    # Have turtle go to 0,0
    t.goto(0, 0)  # Center the drawing roughly
    # Make turtle infinitely fast
    t.speed(0)  # Fastest speed
    t.pendown()
    
    # Get user input for side length and recursion depth
    side_length = int(input("How long do you want each side length to be?: "))
    recursion_depth = int(input("And what's the recursion depth you would like?: "))
    
    draw_sierpinski(side_length, recursion_depth)

main()
turtle.done()