from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_Score = 0
        self.r_Score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_Score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_Score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_Score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_Score += 1
        self.update_scoreboard()
