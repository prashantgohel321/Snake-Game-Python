from turtle import Turtle
import colors

ALIGNMENT = "center"
FONT = ("Lucida Sans", 30, "bold")
# GAME_OVER_COLOR = '#27374D'
# SCORE_COLOR = '#DDE6ED'

class Scoreboard(Turtle):
    """ This class maintains the scoreboard. """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color(colors.SCORE_COLOR)
        self.goto(0, 360)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color(colors.GAME_OVER_COLOR)
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 40, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
