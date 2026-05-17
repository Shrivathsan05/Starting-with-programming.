import math
Angle = input(" Enter an acute angle of a right triangle (less than 90 Degrees) : ")
if Angle.isdigit():
    Angle = int(Angle)
    if Angle < 90:
        rad = math.radians(Angle)
        print("", math.sin(rad), "is the sin value ")
        print("", math.cos(rad), "is the cos value ")
        print("", math.tan(rad), "is the tan value ")
    else:
        print("", Angle, "is not a acute Angle ")
else :
    print("", Angle, "is not a valid Angle ")
