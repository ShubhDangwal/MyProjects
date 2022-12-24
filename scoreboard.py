from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.reupdate()

    def reupdate(self):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score:{self.score}", font=FONT, align='center')
        self.hideturtle()
