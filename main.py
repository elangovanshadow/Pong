# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import time
from paddle import Paddle
from turtle import Screen
from ball import Ball
from score_board import Score_Board

screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor('black')
screen.title('Ping Pong')
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkey(l_paddle.move_up,'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(screen.exitonclick, '1')
speed = 0.1

Score = Score_Board()
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.movement()
    Score.display()




    #Detect collusion with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        speed *= 0.9



    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        speed *= 0.9



    if ball.xcor() > 390:

        ball.refresh()
        ball.bounce_x()
        Score.l_score += 1
        speed = 0.1



    if ball.xcor() < -390 :

        # game_is_on = False
        ball.refresh()
        ball.bounce_x()
        Score.r_score += 1
        speed = 0.1





