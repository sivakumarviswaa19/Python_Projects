FONT = ("Courier", 20, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=1
        self.goto(-250, 250)
        self.write(f"Level = {self.level}",align="left",font=FONT)


    def score(self):
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}",align="left",font=FONT)

