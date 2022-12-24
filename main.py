from turtle import Screen, Turtle
from ball import Ball
from scoreboard import Scoreboard
import time
from food import Food
import random
CONST = 0.1
FONT = ("Courier", 30, "normal")
screen = Screen()
screen.screensize(600, 600, "black")
screen.title("4 BALLS")
screen.tracer(0)
scoreboard = Scoreboard()
food = Food()
turtle = Turtle("turtle")
turtle.color("cyan")
turtle.penup()
turtle.left(90)
turtle.goto(turtle.xcor(), -300)
POSITIONS = [(-340, 300), (340, 300), (-340, -300), (340,  -300)]


def go_up():
    turtle.forward(20)


def go_down():
    turtle.backward(20)


def go_left():
    turtle.left(90)


def go_right():
    turtle.right(90)


balls = []
for i in range(4):
    ball = Ball()
    ball.goto(POSITIONS[i])
    balls.append(ball)

game_is_on = True
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")
while game_is_on:
    POS = (turtle.xcor(), turtle.ycor())
    time.sleep(CONST)
    screen.update()
    for ball in balls:
        ball.move()
    # Detecting collision with walls.
        ball.collision_with_wall()
    # Updating Position of each ball.
        i = 0
        POSITIONS[i] = (ball.xcor(), ball.ycor())
    # checking turtle is within the range.
    if turtle.ycor() > 320:
        turtle.goto(turtle.xcor(), -300)
    elif turtle.ycor() < -320:
        turtle.goto(turtle.xcor(), 300)
    elif turtle.xcor() > 380:
        turtle.goto(-360, turtle.ycor())
    elif turtle.xcor() < -380:
        turtle.goto(360, turtle.ycor())
    # Detecting collision of food and turtle.
    if turtle.distance(food.xcor(), food.ycor()) < 15:
        food.reupdate((random.randint(-320, 320), random.randint(-280, 280)))
        scoreboard.score += 1
        scoreboard.reupdate()
        CONST *= 0.7
        screen.update()
    for ball in balls:
        if ball.check(POS, ball):
            tim = Turtle()
            tim.color("white")
            tim.penup()
            tim.write("GAME OVER", font=FONT, align='center')
            tim.hideturtle()
            game_is_on = False

screen.exitonclick()









