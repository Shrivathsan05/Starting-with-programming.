Seats = int(input(" Pls enter the seating capacity the school bus : "))
SeatFare = int(input(" Pls enter the Cost per seat : "))
MaintPercentage = int(input(" Pls enter Maintainence Percentage : "))

class Vehicle( object ) :
    def __init__(Self, Seat, Cost, MainPer) :
        Self.Seat = Seat
        Self.Cost = Cost
        Self.MainPer = MainPer
    def Display(Self) :
        print("Total Fare Cost per Trip:", Self.Seat*Self.Cost)
class SchoolBus( Vehicle ) :
    def __init__(Self, Seat, Cost, MainPer):
        Self.Seat = Seat
        Self.Cost = Cost
        Self.MainPer = MainPer
        Vehicle.__init__(Self, Seat, Cost, MainPer)
    def Display(Self) :
        super().Display()
        print("Total Fare Cost per Trip including Maintainence:", (Self.Seat*Self.Cost)+(Self.Seat*Self.Cost*Self.MainPer /100))
        print("Total Fare Cost per Ticket including Maintainence:", (((Self.Seat*Self.Cost)+(Self.Seat*Self.Cost*Self.MainPer /100))/Self.Seat))
s = SchoolBus(Seats,SeatFare,MaintPercentage)
s.Display()