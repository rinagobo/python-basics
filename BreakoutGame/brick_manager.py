from turtle import *

colors = ['red', 'orange', 'green', 'yellow']

class BrickManager:
    def __init__(self):
        self.max_bricks = 9
        self.position = [-240, -180, -120, -60, 0, 60, 120, 180, 240]

        self.red_bricks_1 = []
        self.red_bricks_2 = []
        self.orange_bricks_1 = []
        self.orange_bricks_2 = []
        self.green_bricks_1 = []
        self.green_bricks_2 = []
        self.yellow_bricks_1 = []
        self.yellow_bricks_2 = []

    def create_bricks(self):
        for count in range(self.max_bricks):
            self.red_bricks_1.append(Turtle('square'))
            self.red_bricks_1[count].shapesize(stretch_wid=0.5, stretch_len=1.5)
            self.red_bricks_1[count].penup()
            self.red_bricks_1[count].color('red')
            self.red_bricks_1[count].setposition(self.position[count], 150)

        for count in range(self.max_bricks):
            self.red_bricks_2.append(Turtle('square'))
            self.red_bricks_2[count].shapesize(stretch_wid=0.5, stretch_len=1.5)
            self.red_bricks_2[count].penup()
            self.red_bricks_2[count].color('red')
            self.red_bricks_2[count].setposition(self.position[count], 135)

        for count in range(self.max_bricks):
            self.orange_bricks_1.append(Turtle('square'))
            self.orange_bricks_1[count].shapesize(stretch_wid=0.5, stretch_len=1.5)
            self.orange_bricks_1[count].penup()
            self.orange_bricks_1[count].color('orange')
            self.orange_bricks_1[count].setposition(self.position[count], 120)

        for count in range(self.max_bricks):
            self.orange_bricks_2.append(Turtle('square'))
            self.orange_bricks_2[count].shapesize(stretch_wid=0.5, stretch_len=1.5)
            self.orange_bricks_2[count].penup()
            self.orange_bricks_2[count].color('orange')
            self.orange_bricks_2[count].setposition(self.position[count], 105)

        for count in range(self.max_bricks):
            self.green_bricks_1.append(Turtle('square'))
            self.green_bricks_1[count].shapesize(stretch_wid=0.5, stretch_len=1.5)
            self.green_bricks_1[count].penup()
            self.green_bricks_1[count].color('green')
            self.green_bricks_1[count].setposition(self.position[count], 90)

        for count in range(self.max_bricks):
            self.green_bricks_2.append(Turtle('square'))
            self.green_bricks_2[count].shapesize(stretch_wid=0.5, stretch_len=1.5)
            self.green_bricks_2[count].penup()
            self.green_bricks_2[count].color('green')
            self.green_bricks_2[count].setposition(self.position[count], 75)

        for count in range(self.max_bricks):
            self.yellow_bricks_1.append(Turtle('square'))
            self.yellow_bricks_1[count].shapesize(stretch_wid=0.5, stretch_len=1.5)
            self.yellow_bricks_1[count].penup()
            self.yellow_bricks_1[count].color('yellow')
            self.yellow_bricks_1[count].setposition(self.position[count], 60)

        for count in range(self.max_bricks):
            self.yellow_bricks_2.append(Turtle('square'))
            self.yellow_bricks_2[count].shapesize(stretch_wid=0.5, stretch_len=1.5)
            self.yellow_bricks_2[count].penup()
            self.yellow_bricks_2[count].color('yellow')
            self.yellow_bricks_2[count].setposition(self.position[count], 45)