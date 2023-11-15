import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
screen.listen()
screen.onkey(fun=player.move_fd, key="Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
screen.exitonclick()