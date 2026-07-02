#Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog.
from abc import ABC, abstractmethod
class Animal(ABC) :
    def SpecialMove(Self) :
        pass
class Human(Animal) :
    def SpecialMove(Self) :
        print(" I can walk, run, & crawl! ")
class Snake(Animal) :
    def SpecialMove(Self) :
        print(" I can slither! ")
class Dog(Animal) :
    def SpecialMove(Self) :
        print(" I can bark! ")
class Lion(Animal) :
    def SpecialMove(Self) :
        print(" I can roar! ")
MasterWu = Human()
MasterWu.SpecialMove()
TheGreatDevourer = Snake()
TheGreatDevourer.SpecialMove()
Garmadon = Dog()
Garmadon.SpecialMove()
Lloyd = Lion()
Lloyd.SpecialMove()