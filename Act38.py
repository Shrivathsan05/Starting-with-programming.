#Write a program to draw a square inside a square?
import turtle
MyWN = turtle.Screen()
MyWN.bgcolor("Red")
MyWN.title("Turtle")
MyPen = turtle.Turtle()
Size = 0
while True:
    for s in range (4):
        MyPen.fd(Size + 1)
        MyPen.left(90)
        Size = Size - 5
    Size = Size + 1