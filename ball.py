import random
from turtle import Turtle
x_DIST = 10
y_DIST = 10
CHOOSE = [10, 20, 30, 40, 50]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_DIST = 10
        self.y_DIST = 10
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_DIST
        new_y = self.ycor() + self.y_DIST
        self.goto(new_x, new_y)

    def collision_with_wall(self):
        if self.xcor() > 360 or self.xcor() < -360:
            # self.right(random.choice(CHOOSE))
            self.x_DIST *= -1
        if self.ycor() > 300 or self.ycor() < -300:
            # self.left(random.choice(CHOOSE))
            self.y_DIST *= -1

    def check(self,POS,ball):
        if ball.distance(POS) < 15:
            return True