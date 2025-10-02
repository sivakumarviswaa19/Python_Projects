import turtle as t

pos = [(0, 0), (-20, 0), (-40, 0)]
class Snake:

    def __init__(self):
        self.turtles = []

    def make_snakes(self):
        for i in pos:
            self.create(i)

    def create(self,position):
        seg_no = t.Turtle()
        seg_no.color("white")
        seg_no.penup()
        seg_no.shape("square")
        seg_no.goto(position)
        self.turtles.append(seg_no)

    def extend(self):
        self.create(self.turtles[-1].position())



    def move(self):
        for j in range(len(self.turtles) - 1, 0, -1):
            nx = self.turtles[j - 1].xcor()
            ny = self.turtles[j - 1].ycor()
            self.turtles[j].goto(nx, ny)

        self.turtles[0].forward(20)

    def up(self):
        if self.turtles[0].heading()==270:
            pass
        else:
            self.turtles[0].setheading(90)

    def left(self):
        if self.turtles[0].heading()==0:
            pass
        else:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading()==180:
            pass
        else:
            self.turtles[0].setheading(0)

    def down(self):
        if self.turtles[0].heading()==90:
            pass
        else:
            self.turtles[0].setheading(270)


