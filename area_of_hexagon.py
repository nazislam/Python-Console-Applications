#!/usr/bin/env python3

# LoneRanger
# 02/10/19
# Calculating area of a regular hexagon using class

class Hexagon:
    def __init__(self, length):
        self.a = length

    def area(self):
    	area = (3*(3**1/2)*self.a**2)/2
    	return area 

side = int(input('Enter the side of the regular hexagon: '))
hex1 = Hexagon(side)  
areaOfHex = hex1.area()
print(areaOfHex)     
