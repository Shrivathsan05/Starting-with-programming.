#Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.
class Point :
    def __init__(Self, X = 0, Y = 0) :
        Self.x = X
        Self.y = Y
    def __str__(Self) :
        return " ({0}, {1}) ".format(Self.x, Self.y)
Point1 = Point(2, 3)
print(Point1) 