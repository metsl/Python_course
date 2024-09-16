from turtle import Turtle
from snake import Snake
from food import Food
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,280)
        self.score = 0
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
       self.goto(0,0)
       self.hideturtle()
       self.color("white")
       self.write("Game Over!", False, ALIGNMENT, FONT)