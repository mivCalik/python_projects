from turtle import Turtle
ALIGN = "center"
FONT = ("Ariel", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", align= ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGN, font=FONT)
