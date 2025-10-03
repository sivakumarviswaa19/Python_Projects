from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scorecard import Score

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
screen=Screen()
score=Score()

screen.setup(800,600)
screen.bgcolor("black")
screen.listen()

r_paddle.set_controls("Up","Down")
l_paddle.set_controls("w","s")

is_on=True
while is_on:
    screen.update()
    time.sleep(ball.movespeed)
    ball.ballmove()

    #collide with up and down
    if ball.ycor() >= 280 or ball.ycor() <=-280:
        ball.bouncey()

    #collide with wall left and right
    if ball.xcor() >380:
        screen.tracer(0)
        ball.ball_reset()
        score.scoreL()
        score.scorecard()


    if ball.xcor() <-380:
        screen.tracer(0)
        ball.ball_reset()
        score.scoreR()
        score.scorecard()


    #collide with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 :
        ball.bouncex()
        score.scoreR()
        screen.tracer(0)
        score.scorecard()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bouncex()
        score.scoreL()
        screen.tracer(0)
        score.scorecard()

screen.exitonclick()