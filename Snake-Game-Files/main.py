from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("<----Snake Game---->")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        # game_is_on = False
        score.reset_score()
        snake.reset()
    # detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score.reset_score()
            snake.reset()
screen.exitonclick()

