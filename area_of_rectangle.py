#!/usr/bin/env python3

# Naz-Al Islam
# 05/09/16
# Calculating area of a rectangle using class

class Rectangle:
    def __init__(self, length, width):
        self.x = length
        self.y = width

    def area(self):
        return self.x * self.y

rec1 = Rectangle(3, 5)
areaOfRec = rec1.area()
print(areaOfRec)

