from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xm=10
        self.ym=10
        self.movespeed=0.1

    def ballmove(self):
        x=self.xcor()+ self.xm
        y=self.ycor()+ self.ym
        self.goto(x,y)

    def bouncey(self):
        self.ym *= -1
    def bouncex(self):
        self.xm *= -1
        self.movespeed *= 0.9


    #getting ball to origin and changing direction
    def ball_reset(self):
        self.goto(0,0)
        self.movespeed = 0.1
        self.bouncex()






