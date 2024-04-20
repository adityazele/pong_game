from turtle import Turtle


class Scoreboard:

    def __init__(self):
        self.score_pd1 = 0
        self.score_pd2 = 0
        self.draw_dashed_line()
        self.update_score()

    def draw_dashed_line(self):
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.color('white')
        self.tim.goto(0, -169)
        self.tim.setheading(90)
        self.tim.pendown()
        for _ in range(30):
            self.tim.forward(15)
            self.tim.penup()
            self.tim.forward(10)
            self.tim.pendown()

    def update_score(self):
        self.tom_pd1 = Turtle()
        self.tom_pd2 = Turtle()
        self.tom_pd1.hideturtle()
        self.tom_pd2.hideturtle()
        self.tom_pd1.penup()
        self.tom_pd2.penup()
        self.tom_pd1.color('white')
        self.tom_pd2.color('white')
        self.tom_pd1.goto(-50, 120)
        self.tom_pd1.write(self.score_pd1, True, font=('Arial', 30, 'normal'))
        self.tom_pd2.goto(25, 120)
        self.tom_pd2.write(self.score_pd2, True, font=('Arial', 30, 'normal'))
