#Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?
import turtle
turtle.Screen().bgcolor("Gold")
turtle.Screen().setup(300,400)
Polygon = turtle.Turtle()
NumberSides = 6
SideLength = 70
Angle = 360.0 / NumberSides
for s in range (NumberSides):
    Polygon.forward(SideLength)
    Polygon.right(Angle)
turtle.done

