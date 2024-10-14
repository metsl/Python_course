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
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))

    # def game_over(self):
    #    self.goto(0,0)
    #    self.hideturtle()
    #    self.color("white")
    #    self.write("Game Over!", False, ALIGNMENT, FONT)