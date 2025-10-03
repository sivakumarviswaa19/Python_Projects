COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        self.CAR=[]
        self.carspeed=STARTING_MOVE_DISTANCE

    def cars(self):
        #to avoid overcrowding
        if random.randint(1,6) == 1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            # spawn positions for the cars
            x = 280
            y = random.randint(-200, 200)
            new_car.goto(x,y)
            new_car.setheading(new_car.heading()+180)
            self.CAR.append(new_car)


    def carmove(self):
        for i in self.CAR:
            i.forward(self.carspeed)

    def inc_speed(self):
        self.carspeed += MOVE_INCREMENT









