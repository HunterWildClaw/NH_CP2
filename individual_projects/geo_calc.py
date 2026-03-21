# NH 2nd Geo Calc
#Import math cuz yes
import math
import csv
import os

# Base class for all geometric shapes.
class Shape:
    # - Define a parent class that all shapes inherit from
    # - Store the name of the shape
    # - Define placeholder methods for area and perimeter (to be overridden by subclasses)
    # - Define comparison methods for area and perimeter between shapes
    # - Define method to export shape data as CSV row

    def __init__(self, name):
        #Initialize shape with a name
        self.name = name

    def area(self):
        # Return the area of the shape (override in subclass)
        pass

    def perimeter(self):
        #Return the perimeter of the shape (override in subclass)
        pass

    def has_larger_area(self, other):
        # Compare this shape's area with another shape's area
        # Return True if this shape has larger area, False otherwise
        """Compares area with another shape."""
        return self.area() > other.area()

    def has_longer_perimeter(self, other):
        # Compare this shape's perimeter with another shape's perimeter
        # Return True if this shape has longer perimeter, False otherwise
        """Compares perimeter with another shape."""
        return self.perimeter() > other.perimeter()

    def to_csv_row(self):
        # Convert shape data to a dictionary format suitable for CSV export
        # Return dict with shape properties and calculated values
        """Returns shape data as a dictionary for CSV export."""
        pass

class Circle(Shape):
    # - Inherit from Shape
    # - Store radius as instance variable
    # - Validate that radius is positive
    # - Calculate area using formula: π * r²
    # - Calculate perimeter using formula: 2 * π * r
    # - Display circle info in formatted box
    # - Provide formula guide as static method

    def __init__(self, radius, count):
        #Initialize circle with radius and count number
        # Validate radius > 0, raise error if not
        # Call parent constructor with formatted name
        super().__init__(f"Circle #{count}")
        if radius <= 0: raise ValueError("Dimensions must be positive.")
        self.radius = radius

    def area(self):
        #Calculate circle area using π * r²
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        #  Calculate circle circumference using 2 * π * r
        return 2 * math.pi * self.radius

    def to_csv_row(self):
        # Create dictionary with circle data
        # Include name, type, radius, rounded area, rounded perimeter
        return {"Shape": self.name, "Type": "Circle", "Radius": self.radius, "Area": round(self.area(), 2), "Perimeter": round(self.perimeter(), 2)}

    def display_info(self):
        # Print formatted box with circle information
        # Display name, radius, area, and perimeter
        print(f"┌─────────────────────────────────────┐")
        print(f"│ Shape: {self.name:<28} │")
        print(f"│ Radius: {self.radius:<27} │")
        print(f"│ Area: {round(self.area(), 2):<28} │")
        print(f"│ Perimeter: {round(self.perimeter(), 2):<23} │")
        print(f"└─────────────────────────────────────┘")

    @staticmethod
    def formula_guide():
        #  Return string describing circle formulas
        return "Circle: Area = πr², Perimeter = 2πr"

class Rectangle(Shape):
    # - Inherit from Shape
    # - Store length and width as instance variables
    # - Validate that both length and width are positive
    # - Calculate area using formula: length * width
    # - Calculate perimeter using formula: 2 * (length + width)
    # - Display rectangle info in formatted box
    # - Provide formula guide as static method

    def __init__(self, length, width, count):
        # Initialize rectangle with length, width, and count number
        # Validate both dimensions > 0, raise error if not
        # Call parent constructor with formatted name
        super().__init__(f"Rectangle #{count}")
        if length <= 0 or width <= 0: raise ValueError("Dimensions must be positive.")
        self.length = length
        self.width = width

    def area(self):
        # Calculate rectangle area using length * width
        return self.length * self.width

    def perimeter(self):
        #Calculate rectangle perimeter using 2 * (length + width)
        return 2 * (self.length + self.width)

    def to_csv_row(self):
        # Create dictionary with rectangle data
        # Include name, type, length, width, rounded area, rounded perimeter
        return {"Shape": self.name, "Type": "Rectangle", "Length": self.length, "Width": self.width, "Area": round(self.area(), 2), "Perimeter": round(self.perimeter(), 2)}

    def display_info(self):
        # Print formatted box with rectangle information
        # Display name, dimensions as length x width, area, and perimeter
        print(f"┌─────────────────────────────────────┐")
        print(f"│ Shape: {self.name:<28} │")
        print(f"│ Dimensions: {self.length}x{self.width:<20} │")
        print(f"│ Area: {round(self.area(), 2):<28} │")
        print(f"│ Perimeter: {round(self.perimeter(), 2):<23} │")
        print(f"└─────────────────────────────────────┘")

    @staticmethod
    def formula_guide():
        # Return string describing rectangle formulas
        return "Rectangle: Area = l * w, Perimeter = 2(l + w)"

class Square(Rectangle):
    # - Inherit from Rectangle (since square is special rectangle)
    # - Store side as instance variable
    # - Initialize with equal length and width
    # - Override name to show "Square" instead of "Rectangle"
    # - Calculate area using inherited method (side * side)
    # - Calculate perimeter using inherited method (4 * side)
    # - Provide formula guide as static method

    def __init__(self, side, count):
        # Initialize square with side length and count number
        # Call parent constructor with equal length and width
        # Override name to display "Square" instead of "Rectangle"
        # Store side separately for clarity
        super().__init__(side, side, count)
        self.name = f"Square #{count}"
        self.side = side

    def to_csv_row(self):
        # Create dictionary with square data
        # Include name, type, side, rounded area, rounded perimeter
        return {"Shape": self.name, "Type": "Square", "Side": self.side, "Area": round(self.area(), 2), "Perimeter": round(self.perimeter(), 2)}

    @staticmethod
    def formula_guide():
        # Return string describing square formulas
        return "Square: Area = side², Perimeter = 4 * side"

class Triangle(Shape):
    # - Inherit from Shape
    # - Store base, height, and two side lengths as instance variables
    # - Validate that all dimensions are positive
    # - Calculate area using formula: 0.5 * base * height
    # - Calculate perimeter using formula: side_a + side_b + base
    # - Display triangle info in formatted box
    # - Provide formula guide as static method

    def __init__(self, base, height, side_a, side_b, count):
        #Initialize triangle with base, height, two sides, and count number
        # Validate all dimensions > 0, raise error if not
        # Call parent constructor with formatted name
        super().__init__(f"Triangle #{count}")
        if any(x <= 0 for x in [base, height, side_a, side_b]):
            raise ValueError("Dimensions must be positive.")
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        #Calculate triangle area using 0.5 * base * height
        return 0.5 * self.base * self.height

    def perimeter(self):
        #Calculate triangle perimeter using sum of all three sides
        return self.side_a + self.side_b + self.base

    def to_csv_row(self):
        #Create dictionary with triangle data
        # Include name, type, base, height, both sides, rounded area, rounded perimeter
        return {"Shape": self.name, "Type": "Triangle", "Base": self.base, "Height": self.height, "Side A": self.side_a, "Side B": self.side_b, "Area": round(self.area(), 2), "Perimeter": round(self.perimeter(), 2)}

    def display_info(self):
        #Print formatted box with triangle information
        # Display name, area, and perimeter
        print(f"┌─────────────────────────────────────┐")
        print(f"│ Shape: {self.name:<28} │")
        print(f"│ Area: {round(self.area(), 2):<28} │")
        print(f"│ Perimeter: {round(self.perimeter(), 2):<23} │")
        print(f"└─────────────────────────────────────┘")

    @staticmethod
    def formula_guide():
        # Return string describing triangle formulas
        return "Triangle: Area = 0.5 * b * h, Perimeter = a + b + c"

class GeometryCalculator:
    # - Maintain a list of all created shapes
    # - Define CSV file path for saving data
    # - Validate user numerical input with error handling
    # - Save all shapes to CSV file
    # - Create shapes based on user selection
    # - Sort shapes by area or perimeter
    # - Display main menu and handle user commands
    # - Run main event loop

    def __init__(self):
        #Initialize calculator
        # Create empty list to store shapes
        # Set CSV filename for data export
        self.shapes = []
        self.csv_file = "shapes.csv"

    def validate_input(self, prompt):
        # Loop until valid input received
        # Prompt user for input
        # Try to convert input to float
        # Check if value is positive (> 0)
        # If not positive, display error and loop again
        # If not numeric, display error and loop again
        # Return valid positive number
        while True:
            try:
                val = float(input(prompt))
                if val <= 0:
                    print("❌ Error: Value must be positive.")
                    continue
                return val
            except ValueError:
                print("❌ Error: Please enter a valid number.")

    def save_to_csv(self):
        # Check if shapes exist
        # If no shapes, display message and return
        # Open CSV file for writing
        # Create CSV writer with all possible fieldnames
        # Write header row
        # Iterate through shapes and write each row
        # Display success message
        # Catch and display any errors that occur
        """Save all shapes to CSV file."""
        if not self.shapes:
            print("❌ No shapes to save.")
            return
        
        try:
            with open(self.csv_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["Shape", "Type", "Radius", "Length", "Width", "Side", "Base", "Height", "Side A", "Side B", "Area", "Perimeter"])
                writer.writeheader()
                for shape in self.shapes:
                    writer.writerow(shape.to_csv_row())
            print(f"✅ Shapes saved to {self.csv_file}")
        except Exception as e:
            print(f"❌ Error saving to CSV: {e}")

    def create_shape(self):
        # Display menu with shape options
        # Get user choice (1-4)
        # Calculate shape count based on existing shapes
        # Based on choice:
        #   - Get required dimensions from user using validation
        #   - Create appropriate shape object
        # Add shape to shapes list
        # Display success message and shape info
        # Save all shapes to CSV
        # Handle any errors that occur
        print("\n" + "="*37)
        print("🆕 CREATE NEW SHAPE 🆕")
        print("="*37)
        print("[1] Circle ⭕\n[2] Rectangle 📋\n[3] Square ⬜\n[4] Triangle 🔺")
        
        choice = input("\nEnter shape type (1-4): ")
        count = len(self.shapes) + 1

        try:
            if choice == '1':
                #Get radius, create Circle
                r = self.validate_input("Enter radius: ")
                shape = Circle(r, count)
            elif choice == '2':
                #  Get length and width, create Rectangle
                l = self.validate_input("Enter length: ")
                w = self.validate_input("Enter width: ")
                shape = Rectangle(l, w, count)
            elif choice == '3':
                #  Get side length, create Square
                s = self.validate_input("Enter side: ")
                shape = Square(s, count)
            elif choice == '4':
                # Get base, height, and two sides, create Triangle
                b = self.validate_input("Enter base: ")
                h = self.validate_input("Enter height: ")
                s1 = self.validate_input("Enter side A: ")
                s2 = self.validate_input("Enter side B: ")
                shape = Triangle(b, h, s1, s2, count)
            else:
                print("Invalid selection.")
                return

            self.shapes.append(shape)
            print(f"\n✅ {shape.name} created successfully!")
            shape.display_info()
            self.save_to_csv()
        except Exception as e:
            print(f"❌ Error creating shape: {e}")

    def sort_shapes(self):
        # Check if shapes list is empty, return if so
        # Display sort options to user
        # Get user choice
        # If choice is 1, sort shapes by area in descending order
        # Else sort shapes by perimeter in descending order
        # Display success message
        if not self.shapes: return
        print("\nSort by: [1] Area [2] Perimeter")
        choice = input("Choice: ")
        if choice == '1':
            self.shapes.sort(key=lambda x: x.area(), reverse=True)
        else:
            self.shapes.sort(key=lambda x: x.perimeter(), reverse=True)
        print("✅ Shapes sorted (largest to smallest).")

    def run(self):
        # Loop infinitely (until user quits)
        # Display main menu
        # Show current count of shapes
        # Display shape library:
        #   - If no shapes, show "No shapes created yet"
        #   - Else list each shape with its area
        # Display action options
        # Get user choice
        # Based on choice:
        #   - 1: Create new shape
        #   - 2: View all shapes (display info for each)
        #   - 3: Sort shapes
        #   - 4: Show formula guide (display formulas for all shapes)
        #   - 5: Break loop and exit
        while True:
            print("\n" + "="*37)
            print("🔷 MAIN MENU 🔷")
            print("="*37)
            print(f"Current Shapes: {len(self.shapes)} created")
            
            print("\n📊 SHAPE LIBRARY:")
            if not self.shapes:
                print("┌─────────────────────────────────────┐")
                print("│ No shapes created yet               │")
                print("└─────────────────────────────────────┘")
            else:
                for i, s in enumerate(self.shapes):
                    print(f"[{i+1}] {s.name} (Area: {round(s.area(), 2)})")

            print("\n🎯 ACTIONS:")
            print("[1] Create New Shape\n[2] View All Shapes\n[3] Sort Shapes\n[4] Formula Guide\n[5] Quit")
            
            cmd = input("\nEnter choice: ")
            if cmd == '1': self.create_shape()
            elif cmd == '2': 
                for s in self.shapes: s.display_info()
            elif cmd == '3': self.sort_shapes()
            elif cmd == '4':
                print(f"\n{Circle.formula_guide()}\n{Rectangle.formula_guide()}\n{Triangle.formula_guide()}")
            elif cmd == '5': break

# Create instance of GeometryCalculator
# Call run method to start main event loop
calc = GeometryCalculator()
calc.run()