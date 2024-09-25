from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()

screen.screensize(800, 600, bg="black")
screen.title("PingPong")
screen.tracer(0)



r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()