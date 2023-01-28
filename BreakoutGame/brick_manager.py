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

    def create_bricks(self, section, color, y_cor):
        for count in range(self.max_bricks):
            section.append(Turtle('square'))
            section[count].shapesize(stretch_wid=0.5, stretch_len=1.5)
            section[count].penup()
            section[count].color(color)
            section[count].setposition(self.position[count], y_cor)

    def create_all_bricks(self):
        self.create_bricks(self.red_bricks_1, "red", 150)
        self.create_bricks(self.red_bricks_2, "red", 135)
        self.create_bricks(self.orange_bricks_1, "orange", 120)
        self.create_bricks(self.orange_bricks_2, "orange", 105)
        self.create_bricks(self.green_bricks_1, "green", 90)
        self.create_bricks(self.green_bricks_2, "green", 75)
        self.create_bricks(self.yellow_bricks_1, "yellow", 60)
        self.create_bricks(self.yellow_bricks_2, "yellow", 45)