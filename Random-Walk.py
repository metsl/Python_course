import turtle as t
import random

screen = t.Screen()
timmy = t.Turtle()
timmy.shape("turtle")
timmy.width(5)
timmy.speed(5)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(100):
    rn = random.randrange(0,2)
    if rn == 0:
        timmy.left(90)
    elif rn == 1:
        timmy.right(90)
    timmy.forward(30)
    timmy.color(random_color())





screen.exitonclick()