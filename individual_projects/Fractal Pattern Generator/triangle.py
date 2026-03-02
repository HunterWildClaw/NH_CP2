# NH 2nd Make triangle for Fractal Pattern Generator
#import turtle
import turtle

#Make the function
def draw_sierpinski(length, depth):
    if depth == 0:
        # Base case: Draw a simple equilateral triangle
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        # Recursive step: Draw three smaller Sierpinski triangles
        draw_sierpinski(length/2, depth-1)
        turtle.forward(length/2)
        
        draw_sierpinski(length/2, depth-1)
        turtle.backward(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.right(60)
        
        draw_sierpinski(length/2, depth-1)
        turtle.left(60)
        turtle.backward(length/2)
        turtle.right(60)