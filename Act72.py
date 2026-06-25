#Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.
class Employer( object ) :
    def __init__(Self, Name, IDNumber) :
        Self.Name = Name
        Self.IDNumber = IDNumber
    def Display(Self) :
        print(Self.Name)
        print(Self.IDNumber)
class Employee( Employer ) :
    def __init__(Self, Name, IDNumber, Salary, Post):
        Self.Salary = Salary
        Self.Post = Post
        Employer.__init__(Self, Name, IDNumber)
s = Employee(" Rahul ", 886012, 200000, " Intern ")
s.Display()