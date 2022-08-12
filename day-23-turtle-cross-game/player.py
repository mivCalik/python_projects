from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.seth(90)
        self.goto(STARTING_POSITION)
        self.move_distance = MOVE_DISTANCE
        self.finish_y = FINISH_LINE_Y

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + self.move_distance)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - self.move_distance)

    def finish_line_passed(self):
        if self.ycor() >= 270:
            return True
        else:
            return False

    def new_level(self):
        self.goto(STARTING_POSITION)
