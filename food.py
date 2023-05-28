from turtle import Turtle
import random


class Food(Turtle):  # inherits from Turtle class
    def __init__(self):
        super().__init__()
        self.shape("circle")  # shape of food
        self.penup()  # so the turtle doesn't draw
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # makes it smaller
        self.color("blue")
        self.speed("fastest")  # so we don't see the food being created
        self.refresh()

    def refresh(self):  # food goes to a random location on the screen
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
