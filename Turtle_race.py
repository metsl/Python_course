from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height= 400)
user_bet = screen.textinput(title = "Make your bets!", prompt = "Which turtle will win the race? Enter color: ")

color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x= (-240), y= (y_position[i]))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while  is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle won the race!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()