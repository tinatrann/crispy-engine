from turtle import *

sides = int(input("Enter number of sides:"))
angle = 360/sides
color = input("Enter pencolor:")
fill = input("Enter fillcolor:")
number = int(input("Enter the speed:"))

print ("sides:", sides, "angle", angle)

speed(number)
fillcolor(fill)
begin_fill()
for sides in range(sides):
    pencolor(color)
    forward(50)
    right(angle)
    forward(50)
end_fill()
exitonclick()
