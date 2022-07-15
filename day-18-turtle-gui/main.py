from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()

screen = Screen()
screen.colormode(255)


# This color list is obtained by running hirst_color.py 
colors = [(229, 160, 61), (49, 101, 147), (11, 128, 91), (206, 113, 154), (138, 20, 60), (158, 154, 30), (219, 69, 107), (176, 40, 74)]


#  Spinograf(?)

for i in range(120):
    tim.color(choice(colors))
    tim.circle(100)
    tim.left(3)

screen.resetscreen()

# Hirst Dot Painting

tim.penup()

for i in range (10):
    for j in range(10):
        if j == 0:
            tim.goto(-235, -235+50*i)   # 260 = (50*10+20)/2
        else:
            tim.setheading(0)   # set to the right
            tim.forward(50)
        tim.dot(20, choice(colors))  #

screen.exitonclick()



