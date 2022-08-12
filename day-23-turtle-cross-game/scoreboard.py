from turtle import Turtle
FONT = ("Courier", 24, "bold")
POSITION = (0, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.penup()
        self.color("black")
        self.goto(POSITION)
        self.seth(90)
        self.write(arg=f"LEVEL {self.level}", align="center", font=FONT)
        self.draw_lines()

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", False, "center", FONT)

    def draw_lines(self):
        self.penup()
        self.seth(0)
        self.color("gray")
        self.goto(-300, -270)
        self.pendown()
        self.fd(600)
        self.penup()
        self.goto(-300, 270)
        self.pendown()
        self.fd(600)

