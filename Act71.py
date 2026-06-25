#Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.
class Vehicle :
    def __init__(Self, Name, MaximumSpeed, Mileage) :
        Self.Name = Name
        Self.MaximumSpeed = MaximumSpeed
        Self.Mileage = Mileage
class Motorcycle(Vehicle) :
    pass
Attributes = Motorcycle(" Hyundai ", 180, 12)
print(" Vehicle Name :", Attributes.Name, "\n Vehicle Speed :", Attributes.MaximumSpeed, "\n Vehicle Milage :", Attributes.Mileage, "")