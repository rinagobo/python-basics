from turtle import Screen, Turtle
from brick_manager import *
from ball import *
from score_manager import *
import time



####### Create user interface #######
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
brick_manager = BrickManager()
brick_manager.create_all_bricks()
ball = Ball()



####### Functions for the game #######
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

def check_score_point(bricks_name, brick_ycor, point):
    for n in range(0, 9):
        if ball.distance(bricks_name[n]) < 30 and ball.ycor() >= brick_ycor:
            bricks_name[n].reset()
            ball.bounce_y()
            change_speed()
            scoreboard.score_point(point)

# Paddle controller
def go_right():
    new_x = paddle.xcor() + 30
    paddle.goto(new_x, paddle.ycor())

def go_left():
    new_x = paddle.xcor() - 30
    paddle.setposition(new_x, paddle.ycor())

screen.listen()
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")



####### Game logic #######
game_is_on = True
while game_is_on:
    time.sleep(0.5)
    ball.move()

    # Bounce ball
    if ball.xcor() > 235 or ball.xcor() < -235:
        ball.bounce_x()

    if ball.distance(paddle) < 65 and ball.ycor() <= -70:
        ball.bounce_y()

    if ball.ycor() >= 185:
        ball.bounce_y()

    # Check if the user score and update the score board
    check_score_point(bricks_name=brick_manager.yellow_bricks_2, brick_ycor=35, point=1)
    check_score_point(bricks_name=brick_manager.yellow_bricks_1, brick_ycor=50, point=1)
    check_score_point(bricks_name=brick_manager.green_bricks_2, brick_ycor=65, point=3)
    check_score_point(bricks_name=brick_manager.green_bricks_1, brick_ycor=80, point=3)
    check_score_point(bricks_name=brick_manager.orange_bricks_2, brick_ycor=95, point=5)
    check_score_point(bricks_name=brick_manager.orange_bricks_1, brick_ycor=110, point=5)
    check_score_point(bricks_name=brick_manager.red_bricks_2, brick_ycor=125, point=7)
    check_score_point(bricks_name=brick_manager.red_bricks_1, brick_ycor=140, point=7)

    # Show result
    if scoreboard.score == 288:
        scoreboard.clear()
        scoreboard.scorestring = "%s" % "Succeeded!"
        scoreboard.setposition(-60, 250)
        scoreboard.write(scoreboard.scorestring, False, font=('Arial', 15, 'bold'))
        scoreboard.hideturtle()
        game_is_on = False

    if ball.ycor() < -90:
        scoreboard.clear()
        scoreboard.scorestring = "%s" % f"Game Over! Your score was: {scoreboard.score}"
        scoreboard.setposition(-60, 250)
        scoreboard.write(scoreboard.scorestring, False, font=('Arial', 15, 'bold'))
        scoreboard.hideturtle()
        game_is_on = False



screen.exitonclick()