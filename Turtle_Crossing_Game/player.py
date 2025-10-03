STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle,Screen
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        if self.ycor() > 280:
            self.goto(STARTING_POSITION)
            return True
        return False



