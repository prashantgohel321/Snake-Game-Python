
"""This file creates the boundary wall around the game area."""

from turtle import Turtle, Screen
import colors
# WALL_COLOR = '#27374D'

class Wall:
    """ This class creates a wall around the game screen. """
    def __init__(self):
        self.create_wall()

    def create_wall(self):
        wall = Turtle()
        screen = Screen()
        screen.tracer(0)

        wall.penup()
        wall.goto(x=-390, y=-385)
        wall.pendown()
        wall.speed("slow")
        wall.left(90)
        wall.pensize(15)
        wall.pencolor(colors.WALL_COLOR)

        for i in range(4):
            if i == 1:  # Top border
                wall.pensize(60)
            else:
                wall.pensize(20)
            wall.forward(775)
            wall.right(90)
            screen.update()

        wall.hideturtle()
