import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
answer_state = screen.textinput(title="Guess the State", prompt="What's the name of the state?").capitalize()
if answer_state in data["state"].values:
    state_data = data[data["state"] == answer_state]
    print(state_data)
