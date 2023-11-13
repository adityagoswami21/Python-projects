from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
turtle.shape("square")
turtle.shapesize(stretch_wid=5, stretch_len=1)
turtle.color("white")
turtle.penup()
turtle.speed("fastest")
turtle.goto(350, 0)


def move_up():
    new_y = turtle.ycor() + 20
    turtle.goto(turtle.xcor(), new_y)


def move_down():
    new2_y = turtle.ycor() - 20
    turtle.goto(turtle.xcor(), new2_y)


screen.listen()
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
