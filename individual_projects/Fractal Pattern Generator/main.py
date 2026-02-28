#NH 2nd Sierpinski Triangle (TRIFORCE!
import turtle

def draw_sierpinski(length, depth):
    if depth == 0:
        # Base case: Draw a simple equilateral triangle
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        # Recursive step: Draw three smaller Sierpinski triangles
        draw_sierpinski(length / 2, depth - 1)
        turtle.forward(length / 2)
        
        draw_sierpinski(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        
        draw_sierpinski(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

def main():
    # User Customization
    print("--- Sierpinski Triangle Generator ---")
    try:
        user_depth = int(input("Enter recursion depth (recommended 3-6): "))
        user_color = input("Enter a color (e.g., blue, red, green, #FF5733): ").lower()
        
        # Setup the Screen
        screen = turtle.Screen()
        screen.title(f"Sierpinski Triangle - Depth {user_depth}")
        
        # Setup the Turtle
        t = turtle.Turtle()
        t.speed(0)  # Fastest speed
        t.color(user_color)
        t.penup()
        t.goto(-200, -150) # Center the drawing roughly
        t.pendown()

        # Generate the fractal
        draw_sierpinski(400, user_depth)

        print("Drawing complete! Close the graphic window to exit.")
        screen.mainloop()