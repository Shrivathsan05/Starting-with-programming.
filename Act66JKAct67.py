#Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object
class Vehicle :
    def __init__(Self, MaxSpeed, Mileage) :
        Self.MaxSpeed = MaxSpeed
        Self.Mileage = Mileage
ModelXYZMotorcycle = Vehicle(240, 18)
print(" ModelXYZMotorcycle Max Speed :", ModelXYZMotorcycle.MaxSpeed)
print(" ModelXYZMotorcycle Mileage :", ModelXYZMotorcycle.Mileage)