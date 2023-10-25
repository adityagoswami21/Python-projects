from turtle import Turtle, Screen
import turtle
import random
screen = Screen()


# screen.screensize(canvwidth=500, canvheight=400)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
for player in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[player])
    tim.penup()
    tim.goto(x=-230, y=y_positions[player])






screen.exitonclick()
