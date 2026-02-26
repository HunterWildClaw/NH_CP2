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
    t.forward(30)
    t.right(60)
    t.forward(60)
    t.right(60)
    t.forward(60)
    t.right(60)
    t.forward(30)
    t.done()

triangle(int(input("Enter recursion depth (1-5): ")))