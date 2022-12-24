from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.reupdate((random.randint(-320, 320), random.randint(-280, 280)))
    def reupdate(self,POS):
        self.clear()
        self.color("green")
        self.shape("circle")
        self.shapesize(stretch_wid=0.50, stretch_len=0.50)
        self.penup()
        self.goto(POS)