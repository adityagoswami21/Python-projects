from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
turtle = Turtle()
screen = Screen()
ball = Ball()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
screen.exitonclick()
