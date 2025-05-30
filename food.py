
"""This file handles the creation and random placement of food for the snake"""

from turtle import Turtle
import random
import colors

# colors.FOOD_COLOR = "#758694"

class Food(Turtle):
    """ This class generates food at random positions. """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(colors.FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-360, 360)
        random_y = random.randint(-360, 330)
        self.goto(random_x, random_y)
