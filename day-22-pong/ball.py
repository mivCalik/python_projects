from turtle import Turtle
X_MOVE = 10
Y_MOVE = 10
SCREEN_SLEEP = 0.1


class Ball(Turtle):
    def __init__(self, ):
        self.x_change = X_MOVE
        self.y_change = Y_MOVE
        self.screen_sleep = SCREEN_SLEEP
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_change
        new_y = self.ycor() + self.y_change
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        self.y_change = - self.y_change

    def bounce_horizontal(self):
        self.x_change = - self.x_change
        # Speed up ball
        self.x_change *= 1.1
        self.y_change *= 1.1
        self.screen_sleep *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        if self.x_change < 0:
            self.x_change = X_MOVE
        else:
            self.x_change = -X_MOVE

        if self.y_change < 0:
            self.y_change = -Y_MOVE
        else:
            self.y_change = Y_MOVE

        self.screen_sleep = SCREEN_SLEEP

