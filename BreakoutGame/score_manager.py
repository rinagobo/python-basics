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

    def red_point(self):
        self.clear()
        self.score += 7
        self.scorestring = "Score: %s" % self.score
        self.setposition(-60, 250)
        self.write(self.scorestring, False, font=('Arial', 30, 'bold'))
        self.hideturtle()

    def orange_point(self):
        self.clear()
        self.score += 5
        self.scorestring = "Score: %s" % self.score
        self.setposition(-60, 250)
        self.write(self.scorestring, False, font=('Arial', 30, 'bold'))
        self.hideturtle()

    def green_point(self):
        self.clear()
        self.score += 3
        self.scorestring = "Score: %s" % self.score
        self.setposition(-60, 250)
        self.write(self.scorestring, False, font=('Arial', 30, 'bold'))
        self.hideturtle()

    def yellow_point(self):
        self.clear()
        self.score += 1
        self.scorestring = "Score: %s" % self.score
        self.setposition(-60, 250)
        self.write(self.scorestring, False, font=('Arial', 30, 'bold'))
        self.hideturtle()
