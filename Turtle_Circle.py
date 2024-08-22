import turtle as t
import random

screen = t.Screen()
timmy = t.Turtle()
timmy.shape("turtle")
timmy.width(2)
timmy.speed(0)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(72):
    timmy.circle(200)
    timmy.left(5)
    timmy.color(random_color())


screen.exitonclick()