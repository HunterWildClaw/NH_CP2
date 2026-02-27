# NH 2nd Make triangle for Fractal Pattern Generator
#import turtle
import turtle as e

#Set the settings
t=e.Turtle()
s=e.Screen()
t.hideturtle()
t.penup()
#Have turtle go to 0,0
t.goto(0,0)
#Make turtle infinitely fast
t.speed(0)
t.pendown()
t.setheading(180)

#Make the function
def triangle(depth, length):
    t.forward(length/2)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.forward(length/2)
    t.right(60)
    t.penup()
    t.forward(length/4)
    t.pendown()

    if depth > 0:
        triangle(depth-1, length/2)
    else:
        pass

triangle("""int(input("Enter recursion depth (0-5): ")), int(input("And how big would you like the triangle to be? (Side length): "))""")
e.done()