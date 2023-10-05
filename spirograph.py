from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
screen = Screen()
t = Turtle()
t.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

