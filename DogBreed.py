Dog1Name = input(" Enter your 1st dog's name : ")
Dog2Name = input(" Enter your 2nd dog's name : ")
Dog1Species = input(" Enter your 1st dog's species : ")
Dog2Species = input(" Enter your 2nd dog's species : ")
Dog1Color = input(" Enter your 1st dog's color : ")
Dog2Color = input(" Enter your 2nd dog's color : ")
class Dog :
    Species = " Mammal & Canine "
    def __init__(Self, Breed, Color) :
        Self.Breed = Breed
        Self.Color = Color
Remi = Dog( Dog1Species , Dog1Color )
Zephyr = Dog( Dog2Species , Dog2Color )
print( Dog1Name, "is a{}! ".format(Remi.Species))
print( Dog2Name, "is also a{}! ".format(Zephyr.Species))
print( Dog1Name, "is a {} & his color is {}! ".format( Remi.Breed, Remi.Color))
print( Dog2Name, "is a {} & his color is {}! ".format( Zephyr.Breed, Zephyr.Color))