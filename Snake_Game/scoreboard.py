from turtle import Turtle
class score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score=0
        self.goto(0, 280)
        self.hideturtle()

    def scorecount(self):
        self.score +=1
        self.scorecard()

    def scorecard(self):
        self.clear()
        self.write(f"Score ={self.score} ",align="center",font= ("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",26,"normal"))



