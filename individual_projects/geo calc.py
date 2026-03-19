# NH 2nd Geo Calc
#Import math cuz yes
import math
import csv
import os

#Base class for all geometric shapes.
class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

    def has_larger_area(self, other):
        """Compares area with another shape."""
        return self.area() > other.area()

    def has_longer_perimeter(self, other):
        """Compares perimeter with another shape."""
        return self.perimeter() > other.perimeter()

    def to_csv_row(self):
        """Returns shape data as a dictionary for CSV export."""
        pass

class Circle(Shape):
    def __init__(self, radius, count):
        super().__init__(f"Circle #{count}")
        if radius <= 0: raise ValueError("Dimensions must be positive.")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def to_csv_row(self):
        return {"Shape": self.name, "Type": "Circle", "Radius": self.radius, "Area": round(self.area(), 2), "Perimeter": round(self.perimeter(), 2)}

    def display_info(self):
        print(f"┌─────────────────────────────────────┐")
        print(f"│ Shape: {self.name:<28} │")
        print(f"│ Radius: {self.radius:<27} │")
        print(f"│ Area: {round(self.area(), 2):<28} │")
        print(f"│ Perimeter: {round(self.perimeter(), 2):<23} │")
        print(f"└─────────────────────────────────────┘")

    @staticmethod
    def formula_guide():
        return "Circle: Area = πr², Perimeter = 2πr"

class Rectangle(Shape):
    def __init__(self, length, width, count):
        super().__init__(f"Rectangle #{count}")
        if length <= 0 or width <= 0: raise ValueError("Dimensions must be positive.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def to_csv_row(self):
        return {"Shape": self.name, "Type": "Rectangle", "Length": self.length, "Width": self.width, "Area": round(self.area(), 2), "Perimeter": round(self.perimeter(), 2)}

    def display_info(self):
        print(f"┌─────────────────────────────────────┐")
        print(f"│ Shape: {self.name:<28} │")
        print(f"│ Dimensions: {self.length}x{self.width:<20} │")
        print(f"│ Area: {round(self.area(), 2):<28} │")
        print(f"│ Perimeter: {round(self.perimeter(), 2):<23} │")
        print(f"└─────────────────────────────────────┘")

    @staticmethod
    def formula_guide():
        return "Rectangle: Area = l * w, Perimeter = 2(l + w)"

class Square(Rectangle):
    def __init__(self, side, count):
        super().__init__(side, side, count)
        self.name = f"Square #{count}"
        self.side = side

    def to_csv_row(self):
        return {"Shape": self.name, "Type": "Square", "Side": self.side, "Area": round(self.area(), 2), "Perimeter": round(self.perimeter(), 2)}

    @staticmethod
    def formula_guide():
        return "Square: Area = side², Perimeter = 4 * side"

class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, count):
        super().__init__(f"Triangle #{count}")
        if any(x <= 0 for x in [base, height, side_a, side_b]):
            raise ValueError("Dimensions must be positive.")
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side_a + self.side_b + self.base

    def to_csv_row(self):
        return {"Shape": self.name, "Type": "Triangle", "Base": self.base, "Height": self.height, "Side A": self.side_a, "Side B": self.side_b, "Area": round(self.area(), 2), "Perimeter": round(self.perimeter(), 2)}

    def display_info(self):
        print(f"┌─────────────────────────────────────┐")
        print(f"│ Shape: {self.name:<28} │")
        print(f"│ Area: {round(self.area(), 2):<28} │")
        print(f"│ Perimeter: {round(self.perimeter(), 2):<23} │")
        print(f"└─────────────────────────────────────┘")

    @staticmethod
    def formula_guide():
        return "Triangle: Area = 0.5 * b * h, Perimeter = a + b + c"

class GeometryCalculator:
    def __init__(self):
        self.shapes = []
        self.csv_file = "shapes.csv"

    def validate_input(self, prompt):
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
        print("\n" + "="*37)
        print("🆕 CREATE NEW SHAPE 🆕")
        print("="*37)
        print("[1] Circle ⭕\n[2] Rectangle 📋\n[3] Square ⬜\n[4] Triangle 🔺")
        
        choice = input("\nEnter shape type (1-4): ")
        count = len(self.shapes) + 1

        try:
            if choice == '1':
                r = self.validate_input("Enter radius: ")
                shape = Circle(r, count)
            elif choice == '2':
                l = self.validate_input("Enter length: ")
                w = self.validate_input("Enter width: ")
                shape = Rectangle(l, w, count)
            elif choice == '3':
                s = self.validate_input("Enter side: ")
                shape = Square(s, count)
            elif choice == '4':
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
        if not self.shapes: return
        print("\nSort by: [1] Area [2] Perimeter")
        choice = input("Choice: ")
        if choice == '1':
            self.shapes.sort(key=lambda x: x.area(), reverse=True)
        else:
            self.shapes.sort(key=lambda x: x.perimeter(), reverse=True)
        print("✅ Shapes sorted (largest to smallest).")

    def run(self):
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

calc = GeometryCalculator()
calc.run()