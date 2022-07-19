from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Guess the winner.", "Which turtle will finnish first? Type color "
                                                 "(red/orange/yellow/green/blue/purple): ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [75, 45, 15, -15, -45, -75]
turtle_squad = []

for i in range(6):
    new_member = Turtle(shape="turtle")
    new_member.color(colors[i])
    new_member.penup()
    new_member.goto(x=-240, y=y_positions[i])
    turtle_squad.append(new_member)

game_on = False
if user_bet:
    game_on = True

winner = turtle_squad[0]
while game_on:
    for turtle in turtle_squad:
        rand_dist = randint(0,10)
        turtle.forward(rand_dist)

#     Check if game finished
    for turtle in turtle_squad:
        if turtle.xcor() > 230:
            game_on = False
            winner = turtle

winner_color =winner.color()[0]
if winner_color == user_bet:
    print("Lucky guess. You WON 🥳🥳🥳")
else:
    print("You LOSE 😫😫😫")


print("Winner: "+ winner_color + " turtle.")
screen.exitonclick()

