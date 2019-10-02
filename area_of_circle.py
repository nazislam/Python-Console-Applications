#!/usr/bin/env python3

# DarkCoder
# 02/10/19
# Calculating area of a rectangle using class

class Circle:
    def __init__(self, radius):
        self.r = radius
        self.pi = 3.14159265359

    def area(self):
        return 2 * self.r * self.r * self.pi


input_radius = float(input('Enter the radius of the circle: '))

circ1 = Circle(input_radius)
areaOfCircle = circ1.area()
print("The area of the circle is: " + str(areaOfCircle))

