from turtle import Turtle


class Paddle:

    def __init__(self):
        self.pd1 = Turtle('square')
        self.pd1.setheading(90)
        self.pd1.penup()
        self.pd1.color('white')
        self.pd1.shapesize(1, 5)
        self.pd1.goto(-280, 0)

        self.pd2 = Turtle('square')
        self.pd2.setheading(90)
        self.pd2.penup()
        self.pd2.color('white')
        self.pd2.shapesize(1, 5)
        self.pd2.goto(280, 0)

    def up_pd1(self):
        self.pd1.forward(10)

    def down_pd1(self):
        self.pd1.backward(10)

    def up_pd2(self):
        self.pd2.forward(10)

    def down_pd2(self):
        self.pd2.backward(10)
