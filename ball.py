from turtle import Turtle

class Ball:

    def __init__(self):
        self.ball = Turtle('circle')
        self.ball.penup()
        self.ball.color('white')
        self.x = 0
        self.y = 0
        self.bouncey = 1
        self.bouncex = 1

    def move(self):
        self.ball.goto(self.x,self.y)
        self.x += 10 * self.bouncex
        self.y += 10 * self.bouncey
        if self.ball.ycor() > 150:
            self.bouncey = -1
        if self.ball.ycor() < -150:
            self.bouncey = 1
