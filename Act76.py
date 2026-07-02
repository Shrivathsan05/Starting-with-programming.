#Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.
from abc import ABC, abstractmethod
class AbstractClass(ABC) :
    def Print(Self, X) :
        print(" Passed Value :", X)
    @abstractmethod
    def Task(Self) :
        print(" We are inside the abstract class's task! ")
class TestClass(AbstractClass) :
    def Task(Self) :
        print(" We are inside the test class's task! ")
TestClassesObject = TestClass()
TestClassesObject.Task()
TestClassesObject.Print(100)