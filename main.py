# 17/4/2024

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.bgcolor('black')
screen.title('pong game')
screen.setup(width=600, height=350)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.up_pd1, 'w')
screen.onkey(paddle.down_pd1, 's')
screen.onkey(paddle.up_pd2, 'Up')
screen.onkey(paddle.down_pd2, 'Down')

while game_is_on:

    if ball.ball.xcor() > 300:
        scoreboard.score_pd1 += 1
        scoreboard.tom_pd1.clear()
        scoreboard.tom_pd2.clear()
        scoreboard.update_score()
        ball.ball.goto(0, 0)
        ball.x = 0
        ball.y = 0
        ball.bouncex = -1

    if ball.ball.xcor() < -300:
        scoreboard.score_pd2 += 1
        scoreboard.tom_pd1.clear()
        scoreboard.tom_pd2.clear()
        scoreboard.update_score()
        ball.ball.goto(0, 0)
        ball.x = 0
        ball.y = 0
        ball.bouncex = 1

    if -40 < ball.ball.xcor() - paddle.pd2.xcor() < 40 and -50 < ball.ball.ycor() - paddle.pd2.ycor() < 50:
        ball.bouncex = -1

    if -40 < ball.ball.xcor() - paddle.pd1.xcor() < 40 and -50 < ball.ball.ycor() - paddle.pd1.ycor() < 50:
        ball.bouncex = 1
    ball.move()
    time.sleep(0.05)
    screen.update()

screen.exitonclick()
