#!/usr/bin/env python3

# Naz-Al Islam
# 04/18/16
# Car racing game


class Car:

    def __init__(self, start_pos, speed):
        self.carPos = start_pos
        self.carSpeed = speed

    def drive(self, time, direction):
        self.drvTime = time
        self.drvDirection = direction
        if self.drvDirection == 'forward':
            self.carPos = self.carPos + self.drvTime * self.carSpeed
        elif self.drvDirection == 'backward':
            self.carPos = self.carPos - self.drvTime * self.carSpeed

    def printPosition(self):
        print('The car is currently at position ' + str(self.carPos))


def main():
    myCar = Car(2, 3)        
    myCar.printPosition()
    myCar.drive(3, 'forward')
    myCar.printPosition()
    myCar.drive(2, 'backward')
    myCar.printPosition()

    print()

    newCar = Car(5, 7)
    newCar.printPosition()
    newCar.drive(4, 'forward')
    newCar.printPosition()
    newCar.drive(3, 'backward')
    newCar.printPosition()
    newCar.drive(1, 'backward')
    newCar.printPosition()


if __name__ == '__main__':
    main()
