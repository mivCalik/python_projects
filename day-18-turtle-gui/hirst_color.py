import colorgram
from turtle import Screen, Turtle
from random import choice

colors = colorgram.extract("image.jpg", 10)
tim = Turtle()

color_list = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    color_list.append((r, g, b))

print(color_list)
