import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
player=Player()
SCORE=Scoreboard()
car=CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)


def up():
    player.move()

screen.listen()
screen.onkey(up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.tracer(0)
    car.cars()
    car.carmove()

    #detection of turtle with car
    for i in car.CAR:
        if player.distance(i)<25:
            player.goto(0,0)
            player.hideturtle()
            player.write("GAME OVER",align="center",font=("Courier",20,"bold"))
            game_is_on=False


    #moving to next level
    if player.next_level():
        car.inc_speed()
        SCORE.score()






screen.exitonclick()
