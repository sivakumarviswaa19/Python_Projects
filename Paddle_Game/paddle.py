from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        self.position=position
        super().__init__()
        self.color("white")
        self.shapesize(5,1)
        self.speed("fast")
        self.penup()
        self.shape("square")
        self.goto(position)


    def set_controls(self,U,D):
        self.screen.listen()
        def up():
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

        def down():
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

        #assigning keys
        self.screen.onkey(up,U)
        self.screen.onkey(down,D)

