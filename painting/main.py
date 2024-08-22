import colorgram
import turtle as t
import random

colors = colorgram.extract("image.jpg", 30)

#extracting color tuples from the image
# print(colors)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
# print(rgb)

color_list = [(1, 12, 30), (53, 25, 17), (218, 127, 107), (10, 105, 159), (241, 213, 69), (149, 84, 39), (214, 87, 64), (164, 161, 32), (158, 6, 24), (157, 62, 102), (11, 64, 32), (98, 6, 19), (206, 74, 104), (11, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (159, 34, 24), (3, 213, 207), (10, 140, 86), (145, 227, 216), (121, 193, 149), (102, 219, 229), (221, 178, 216), (253, 196, 0), (80, 134, 179)]
print(color_list[1])

screen = t.Screen()
timmy = t.Turtle()
timmy.shape("turtle")
timmy.width(20)
timmy.speed(5)
t.colormode(255)
screen.setworldcoordinates(-1, -1, screen.window_width() - 50, screen.window_height() - 50)

def new_line_left():
    timmy.left(90)
    timmy.penup()
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.pendown()

def new_line_right():
    timmy.right(90)
    timmy.penup()
    timmy.forward(50)
    timmy.right(90)
    timmy.forward(50)
    timmy.pendown()

d = 0
for _ in range(10):
    for n in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        if n == 9:
            d += 1
            if d % 2 == 0:
                new_line_right()
            else:
                new_line_left()




screen.exitonclick()