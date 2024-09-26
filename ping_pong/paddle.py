from turtle import Turtle
SHIFT = 20
# X_COR_LEFT = -350
# X_COR_RIGHT = 350


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.resizemode("user")
        self.turtlesize(5,1)
        self.color("white")
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + SHIFT
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - SHIFT
        self.goto(self.xcor(), new_y)