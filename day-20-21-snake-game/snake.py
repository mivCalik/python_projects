from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_arr = []
        for i in range(3):
            self.extend_size(STARTING_POSITIONS[i])
        self.head = self.snake_arr[0]

    def move(self):
        for i in range(len(self.snake_arr) - 1, 0, -1):
            # we go from tail to head

            new_x = self.snake_arr[i - 1].xcor()
            new_y = self.snake_arr[i - 1].ycor()

            self.snake_arr[i].goto(new_x, new_y)
        self.snake_arr[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend_size(self, position=None):  # position is a tuple

        if position is None:
            tail_x = self.snake_arr[len(self. snake_arr) -1].xcor()
            tail_y = self.snake_arr[len(self.snake_arr) - 1].ycor()
            position = (tail_x, tail_y)
        new_turtle = Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.goto(position)

        self.snake_arr.append(new_turtle)


