import math
pi = math.pi

class Circle:
    def __init__(self, radius=1,):

            self.radius = radius
            self.diameter = radius*2

    def area(self):
        return pi*self.radius**2

    def perimeter(self):
        return 2*pi*self.radius

    def display(self):
        print(f"The area of your circle is {self.area()} and the value of your perimeter is {self.perimeter()}")

Radius = float(input("Enter the radius:"))
circle = Circle(radius=Radius)

circle.display()