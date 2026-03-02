#NH 2nd Fractal Pattern Generator color changer

#Make the color function
def color_setter():
    #ask user what color they want for their Sierpinski Triangle 
    color = input("What color would you like your triangle to be? (Red. Orange, Yellow, Green, Blue, Teal, Purple, Pink, or just Black)\nEnter here: ").title().strip()
    return color