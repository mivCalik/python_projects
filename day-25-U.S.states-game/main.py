from turtle import *
import pandas as pd

data = pd.read_csv("50_states.csv")
state_list = list(data["state"])
# print(data)

screen = Screen()
screen.title("- U.S. State Game -")
screen.bgpic("blank_states_img.gif")

writer = Turtle()
writer.penup()
writer.hideturtle()
writer.seth(90)


def show_state(name):
    state = data[data.state == name]
    state_x = int(state.x)
    state_y = int(state.y)
    writer.goto(state_x, state_y)
    writer.write(name)

# def mouse_click_coor(x, y):
#     print(x,y)
#
# screen.onscreenclick(mouse_click_coor)

score = 0
header = "Guess the State:"
guessed_states = []
while score < 50:
    input = screen.textinput(header, "State Name: ")
    if input is None:
        print(guessed_states)
        print(f"You guessed {score}/50 States.")
        break
    else:
        state_guess = input.title()
        if state_guess in state_list:
            if state_guess in guessed_states:
                header = f"Already said.. {score}/50"
                continue
            score += 1
            header = f"{score}/50 States found"
            show_state(state_guess)
            guessed_states.append(state_guess)
            # print(guessed_states)
        else:
            header = f"Try Again! {score}/50"






# if user entry in state_list
#     write and score +1
#
# else ask again




