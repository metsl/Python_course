import turtle as t
import random
timmy = t.Turtle()
timmy.shape("turtle")
timmy.width(10)
timmy.speed(5)

colors = ["red", "blue", "yellow", "brown", "green", "purple", "orange", "green"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)






screen = t.Screen()
screen.exitonclick()