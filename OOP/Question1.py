#  Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius**2
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


def main():
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)

    print(f"Area of the circle: {circle.area():.2f}")
    print(f"Perimeter of the circle: {circle.perimeter():.2f}")


if __name__ == "__main__":
    main()
