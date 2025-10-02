import turtle as t
import snake
from food import Food
import random
import time
from scoreboard import score


snake = snake.Snake()
screen = t.Screen()
food=Food()
score=score()

screen.listen()
screen.title("Snake Game !")
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")

snake.make_snakes()

screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.turtles[0].distance(food) < 15:

        score.scorecount()
        snake.extend()
        food.refresh()

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() <-280 or snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() < -280:
        is_game_on=False
        score.game_over()

    for e in snake.turtles[1::]:

        if snake.turtles[0].distance(e) < 10:
            is_game_on=False
            score.game_over()




screen.exitonclick()
