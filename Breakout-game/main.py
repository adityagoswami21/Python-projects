from turtle import Turtle, Screen
from bricks import BrickManager
from paddle import Paddle
from ball import Ball
import time
turtle = Turtle()
screen = Screen()
screen.tracer(0)
ball = Ball()
brick_manager = BrickManager()
create_bricks = brick_manager.create_bricks()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
paddle = Paddle((0, -250))

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 270:
        ball.bounce_y()
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 40 and ball.ycor() > -250:
        ball.bounce_y()
        ball.move_speed *= 0.9  # Increase speed after hitting the paddle

    # Detect if the ball goes out of bounds
    if ball.ycor() < -300:
        ball.penup()
        ball.reset_position(paddle.position()+ (0, 30))
        ball.move_speed = 0.1
    
    # detect collision with bricks (not implemented yet)
    for brick in brick_manager.bricks:
        if ball.distance(brick) < 40:
            ball.bounce_y()
            brick.goto(1000, 1000)  # Move the brick off-screen
            brick_manager.bricks.remove(brick)  # Remove the brick from the list
        
            