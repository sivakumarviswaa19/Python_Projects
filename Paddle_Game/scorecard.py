from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scorer = 0
        self.scorel = 0


    def scoreR(self):
        self.scorer += 1
    def scoreL(self):
        self.scorel+=1
    def scorecard(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(100,200)
        self.color("white")

        self.write(self.scorer,align="center",font=("courier",80,"normal"))

        self.goto(-100,200)
        self.write(self.scorel, align="center", font=("courier", 80, "normal"))



