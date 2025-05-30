
"""This file is responsible for creating the snake and managing its movement and extension."""

from turtle import Turtle
import colors

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # initially: 3 segments
MOVE_DISTANCE = 20

# Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Colors
# FIRST_SEGMENT_COLOR = '#27374D'
# BODY_COLOR = '#526D82'

class Snake:
    """ This class creates a snake body and contains methods for movement and extension. """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ Creates the initial snake body. """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """ Adds a new segment to the snake. """
        new_segment = Turtle(shape="square")
        new_segment.color(colors.BODY_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.segments[0].color(colors.FIRST_SEGMENT_COLOR)

    def extend(self):
        """ Adds a new segment to the snake's body. """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Moves the snake forward. """
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """ Turns the snake's head upwards. """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ Turns the snake's head downwards. """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ Turns the snake's head to the left. """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ Turns the snake's head to the right. """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
