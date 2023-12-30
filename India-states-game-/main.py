import turtle
import pandas as pd
screen = turtle.Screen()
image = "India-state.gif"
screen.setup(500, 500)
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("28_states.csv")
all_states = data.state.values
guessed_state = []
while len(guessed_state) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/28 states", prompt="Guess the state").title()
    if answer_state in all_states:
        guessed_state.append(answer_state)
screen.exitonclick()