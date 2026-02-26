# NH 2nd Make triangle for Fractal Pattern Generator
#import turtle
import turtle as e

#Make the function
def triangle(depth):
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
    t.forward(300)
    t.right(120)
    t.forward(600)
    t.right(120)
    t.forward(600)
    t.right(120)
    t.forward(300)
    e.done()
    if depth >0:
        
triangle(int(input("Enter recursion depth (0-5): ")))