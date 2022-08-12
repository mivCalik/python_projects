import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

TIME_SLOWING_FACTOR = 0.85
INITIAL_SLEEP_TIME = 0.1


def car_crash():
    distance = 0
    for car in car_manager.cars:
        y_distance = abs(car.ycor() - player.ycor())
        x_distance = abs(car.xcor() - player.xcor())
        if y_distance < 20 and x_distance < 30:
            return True
    return False


sleep_time = INITIAL_SLEEP_TIME
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=player.go_up)
# screen.onkeypress(key="Down", fun=player.go_down)

game_is_on = True
while game_is_on:
    car_manager.move_cars()
    car_manager.add_car()
    screen.update()

    if car_crash():
        game_is_on = False
        scoreboard.game_over()
        screen.exitonclick()

    if player.finish_line_passed():
        player.new_level()
        scoreboard.increase_level()
        scoreboard.print_score()
        sleep_time *= TIME_SLOWING_FACTOR


    time.sleep(0.1)


