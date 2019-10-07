#!/usr/bin/env python3

# Novojit Saha
# 02/10/19
# Calculating area of a trapezium using class

class Trapezium:
    def __init__(self, base1, base2, height):
        self.x = base1
        self.y = base2
        self.z = height

    def area(self):
        return 0.5 * (self.x + self.y) * self.z


input_base_1 = float( input('Base one value:') )
input_base_2 = float( input('Base two value:') )
input_height = float( input('Height value:') )

trap1 = Trapezium(input_base_1, input_base_2, input_height )
areaOfTrap1 = trap1.area()
print("The area of the trapezium is " + str(areaOfTrap1))