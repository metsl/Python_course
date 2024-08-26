from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.pensize(10)
tim.pencolor("yellow")

def move_f():
    tim.forward(10)

def move_b():
    tim.bk(10)

def clock_w():
    tim.right(10)

def counter_c():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkeypress(move_f, "w")
screen.onkeypress(move_b, "s")
screen.onkeypress(clock_w, "d")
screen.onkeypress(counter_c, "a")
screen.onkeypress(clear, "c")
screen.listen()
screen.exitonclick()





