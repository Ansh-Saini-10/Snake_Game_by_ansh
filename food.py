from turtle import Screen, Turtle
import random

screen = Screen()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        screen.tracer(0)
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.penup()
        self.shape("circle")
        self.color("coral")
        self.teleport()
        screen.update()

    def teleport(self):
        self.goto(x=random.randint(-380, 380), y=random.randint(-280, 280))