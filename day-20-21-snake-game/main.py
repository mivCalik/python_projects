from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

simon = Snake()
berry = Food()
board = Scoreboard()

screen.update()
screen.listen()
screen.onkey(simon.up, "Up")
screen.onkey(simon.down, "Down")
screen.onkey(simon.left, "Left")
screen.onkey(simon.right, "Right")

game_is_on = True
while game_is_on:
    simon.move()
    screen.update()
    time.sleep(0.15)

    # detect collision with berry
    if simon.head.distance(berry) < 15:
        print("nom nom nom...")
        berry.refresh()
        board.increase_score()
        simon.extend_size()

    # detect collision with wall
    simon_x = simon.head.xcor()
    simon_y = simon.head.ycor()
    if simon_x > 280 or simon_x < -280 or simon_y > 280 or simon_y < -280:
        game_is_on = False
        board.game_over()

    # detect collision with body
    for square in simon.snake_arr[1:]:
        if simon.head.distance(square) < 10:
            game_is_on = False
            board.game_over()

screen.exitonclick()
