from turtle import Turtle

class ScoreManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.score = 0
        self.scorestring = "Score: %s" %self.score
        self.setposition(-60, 250)
        self.write(self.scorestring, False, font=('Arial', 30, 'bold'))
        self.hideturtle()

    def score_point(self, point):
        self.clear()
        self.score += point
        self.scorestring = "Score: %s" % self.score
        self.setposition(-60, 250)
        self.write(self.scorestring, False, font=('Arial', 30, 'bold'))
        self.hideturtle()

