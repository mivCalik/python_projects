from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.r_score = 0
        self.l_score = 0
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update()

    def update_score_l(self):
        self.l_score += 1
        self.update()

    def update_score_r(self):
        self.r_score += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        print(f"{self.l_score}:{self.r_score}")



