import math
Pi = round(math.pi, 2)
class Circle :
    def __init__( Self, Radius ) :
        Self.Radius = Radius
def Area(S) :
    return Pi * (S * S)
def Perimeter(S) :
    return 2 * Pi * S
RadiusMainInput = int(input(" Enter the radius of your circle : "))
Radius = Circle(RadiusMainInput)
print(" The area of your circle is :", Area(Radius.Radius))
print(" The perimeter of your circle is :", Perimeter(Radius.Radius))