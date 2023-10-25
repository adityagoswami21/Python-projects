from turtle import Turtle, Screen
import random
screen = Screen()

is_race_on = False
# screen.screensize(canvwidth=500, canvheight=400)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
for player in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[player])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[player])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_pace = random.randint(0,10)
        turtle.fd(random_pace)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win, the winner is {winning_color}")
            else:
                print(f"You loose, the winner is {winning_color}")
            break









screen.exitonclick()
