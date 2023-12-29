import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.values
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="What's the name of the state?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        state_data = data[data.state == answer_state]
        marker.goto(int(state_data.x), int(state_data.y))
        marker.write(answer_state)
    elif answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        missing_data = pandas.DataFrame(missing_state)
        missing_data.to_csv("missed states.csv")
        break

screen.exitonclick()