from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall
import time
import colors

# Constants
# BG_COLOR = '#DDE6ED'
LEFT_X, RIGHT_X = -382, 380
UP_Y, DOWN_Y = 370, -380
MOVE_DELAY = 0.1

# Screen setup
screen = Screen()
screen.setup(width=850, height=850)
screen.bgcolor(colors.BG_COLOR)
screen.title("Snake Game")

# Objects initialization
wall = Wall()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.tracer(0)

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(MOVE_DELAY)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Collision with wall
    if (snake.head.xcor() > RIGHT_X or snake.head.xcor() < LEFT_X or
            snake.head.ycor() > UP_Y or snake.head.ycor() < DOWN_Y):
        game_is_on = False
        scoreboard.game_over()

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
