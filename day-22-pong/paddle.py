from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.seth(90)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.seth(90)
        self.forward(20)

    def move_down(self):
        self.seth(270)
        self.forward(20)
