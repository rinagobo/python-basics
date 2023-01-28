from turtle import Screen, Turtle
from brick_manager import *
from ball import *
from score_manager import *
import time

screen = Screen()
screen.title("Breakout Game")
screen.setup(width=500, height=600)
screen.bgcolor('black')

top_wall = Turtle()
top_wall.shape('square')
top_wall.color('grey')
top_wall.shapesize(stretch_wid=1, stretch_len=25)
top_wall.penup()
top_wall.goto(0, 200)

paddle = Turtle()
paddle.shape('square')
paddle.color('blue')
paddle.shapesize(stretch_wid=0.5, stretch_len=5)
paddle.penup()
paddle.goto(0, -80)

scoreboard = ScoreManager()

ball= Ball()
def change_speed():
    if scoreboard.score >= 4:
        ball.speed(6)
    if scoreboard.score >= 10:
        ball.speed(8)
    if scoreboard.score >= 55:
        ball.speed(10)
    if scoreboard.score >= 110:
        ball.speed(0)
    else:
        pass

brick_manager = BrickManager()
brick_manager.create_all_bricks()

def go_right():
    new_x = paddle.xcor() + 30
    paddle.goto(new_x, paddle.ycor())

def go_left():
    new_x = paddle.xcor() - 30
    paddle.setposition(new_x, paddle.ycor())

screen.listen()
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.5)
    ball.move()

    if ball.xcor() > 235 or ball.xcor() < -235:
        ball.bounce_x()

    if ball.distance(paddle) < 65 and ball.ycor() <= -70:
        ball.bounce_y()

    if ball.ycor() >= 185:
        ball.bounce_y()

    for n in range(0, 9):
        if ball.distance(brick_manager.yellow_bricks_2[n]) < 30 and ball.ycor() >= 35:
            brick_manager.yellow_bricks_2[n].reset()
            ball.bounce_y()
            change_speed()
            scoreboard.score_point(1)

    for n in range(0, 9):
        if ball.distance(brick_manager.yellow_bricks_1[n]) < 30 and ball.ycor() >= 50:
            brick_manager.yellow_bricks_1[n].reset()
            ball.bounce_y()
            change_speed()
            scoreboard.score_point(1)

    for n in range(0, 9):
        if ball.distance(brick_manager.green_bricks_2[n]) < 30 and ball.ycor() >= 65:
            brick_manager.green_bricks_2[n].reset()
            ball.bounce_y()
            change_speed()
            scoreboard.score_point(3)

    for n in range(0, 9):
        if ball.distance(brick_manager.green_bricks_1[n]) < 30 and ball.ycor() >= 80:
            brick_manager.green_bricks_1[n].reset()
            ball.bounce_y()
            change_speed()
            scoreboard.score_point(3)

    for n in range(0, 9):
        if ball.distance(brick_manager.orange_bricks_2[n]) < 30 and ball.ycor() >= 95:
            brick_manager.orange_bricks_2[n].reset()
            ball.bounce_y()
            change_speed()
            scoreboard.score_point(5)

    for n in range(0, 9):
        if ball.distance(brick_manager.orange_bricks_1[n]) < 30 and ball.ycor() >= 110:
            brick_manager.orange_bricks_1[n].reset()
            ball.bounce_y()
            change_speed()
            scoreboard.score_point(5)

    for n in range(0, 9):
        if ball.distance(brick_manager.red_bricks_2[n]) < 30 and ball.ycor() >= 125:
            brick_manager.red_bricks_2[n].reset()
            ball.bounce_y()
            change_speed()
            scoreboard.score_point(7)

    for n in range(0, 9):
        if ball.distance(brick_manager.red_bricks_1[n]) < 30 and ball.ycor() >= 140:
            brick_manager.red_bricks_1[n].reset()
            ball.bounce_y()
            change_speed()
            scoreboard.score_point(7)

    if scoreboard.score == 288:
        scoreboard.clear()
        scoreboard.scorestring = "%s" % "Succeeded!"
        scoreboard.setposition(-60, 250)
        scoreboard.write(scoreboard.scorestring, False, font=('Arial', 30, 'bold'))
        scoreboard.hideturtle()
        game_is_on = False

    if ball.ycor() < -90:
        scoreboard.clear()
        scoreboard.scorestring = "%s" % "Game Over!"
        scoreboard.setposition(-60, 250)
        scoreboard.write(scoreboard.scorestring, False, font=('Arial', 30, 'bold'))
        scoreboard.hideturtle()
        game_is_on = False




screen.exitonclick()