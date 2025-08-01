from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
turtle = Turtle()
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect if R paddle misses
    elif ball.xcor() > 380:
        ball.restart()
        scoreboard.l_winner()
    # Detect if L paddle misses
    elif ball.xcor() < -380:
        ball.restart()
        scoreboard.r_winner()
    # elif l_winner
screen.exitonclick()
