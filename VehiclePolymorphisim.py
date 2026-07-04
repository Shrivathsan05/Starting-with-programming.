class F1 :
    def __init__(Self, FuelType, MaximumSpeed, DistancePerHour):
        Self.FuelType = FuelType
        Self.MaximumSpeed = MaximumSpeed
        Self.DistancePerHour = DistancePerHour
    def TheFuelType(Self) :
        print(" My Fuel Type Is :", Self.FuelType)
    def TheMaximumSpeed(Self) :
        print(" My Maximum Speed Is :", Self.MaximumSpeed)
    def TheDistancePerHour(Self) :
        print(" My Distance Per Hour Is Calculated In :", Self.DistancePerHour)
class Lamborghini :
    def __init__(Self, FuelType, MaximumSpeed, DistancePerHour):
        Self.FuelType = FuelType
        Self.MaximumSpeed = MaximumSpeed
        Self.DistancePerHour = DistancePerHour
    def TheFuelType(Self) :
        print(" My Fuel Type Is :", Self.FuelType)
    def TheMaximumSpeed(Self) :
        print(" My Maximum Speed Is :", Self.MaximumSpeed)
    def TheDistancePerHour(Self) :
        print(" My Distance Per Hour Is Calculated In :", Self.DistancePerHour)
TheLamborghini = Lamborghini("Premium Unleaded Petrol AKA Gasoline In The USA ", 221, "Miles Per Hour ")
TheFormula1 = F1("Advanced Sustainable Fuel ", 234.88, "Miles Per Hour ")
for Cars in (TheFormula1, TheLamborghini) :
    Cars.TheFuelType()
    Cars.TheMaximumSpeed()
    Cars.TheDistancePerHour()