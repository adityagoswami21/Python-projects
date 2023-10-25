from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
screen = Screen()

def ran_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color
# screen.screensize(canvwidth=500, canvheight=400)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race?")
tim = Turtle()
tom = Turtle()
ani = Turtle()
sim = Turtle()
adi = Turtle()
shi = Turtle()
vee = Turtle()
turtle_list = [tim, tom, ani, sim, adi, shi, vee]
for player in turtle_list:
    player.color(ran_color())
    player.shape("turtle")
    player.penup()
    player.goto(x=-200, y=random.randint(-150,150))





screen.exitonclick()
