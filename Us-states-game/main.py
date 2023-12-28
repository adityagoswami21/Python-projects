import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.values
answer_state = screen.textinput(title="Guess the State", prompt="What's the name of the state?").capitalize()
if answer_state in all_states:
    marker = turtle.Turtle()
    marker.hideturtle()
    marker.penup()
    state_data = data[data.state == answer_state]
    marker.goto(int(state_data.x), int(state_data.y))
    marker.write(state_data.state)
screen.exitonclick()