from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard
END_SCORE = 5

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.update()

#  BINDING EVENTS TO KEYS
screen.listen()

screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")


while scoreboard.r_score < END_SCORE and scoreboard.l_score < END_SCORE:

    # WALL BOUNCE
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()

    if r_paddle.xcor() - ball.xcor() < 25 and abs(r_paddle.ycor() - ball.ycor()) <= 50 and ball.x_change > 0:
        # COLLISION WITH r_paddle
        ball.bounce_horizontal()
    elif ball.xcor() - l_paddle.xcor() < 25 and abs(l_paddle.ycor() - ball.ycor()) <= 50 and ball.x_change < 0:
        # COLLISION WITH l_paddle
        ball.bounce_horizontal()

    if ball.xcor() > 380:
        # lose a point to opponent
        ball.reset_position()
        scoreboard.update_score_l()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_score_r()

    ball.move()
    screen.update()
    sleep(0.1)


screen.exitonclick()
