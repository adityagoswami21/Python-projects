import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=player.move_fd, key="Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.display_cars()
    car_manager.move_cars()
    # Detecting for new level
    if player.new_level():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.clear()
        scoreboard.level_score()
        # scoreboard.new_level += 1
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
