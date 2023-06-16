from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle(image)


data = pandas.read_csv("50_states.csv")
state_name = data["state"]
all_state  = state_name.tolist()
guessed_state = []
i = 0
while len(guessed_state) < 50:
    answer_input = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="whats another state's name?").title()

    # state_x = int(data["x"][data["state"] == answer_input].values)
    # state_y = int(data["y"][data["state"] == answer_input].values)
    # print(state_y)
    # print(state_x)

    if answer_input == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        missing_data = pandas.DataFrame(missing_state)
        missing_data.to_csv("new_learn)_states.csv")
        break

    for j in state_name:
        if j == answer_input:
            t = Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data["state"] == answer_input]
            t.goto(int(state_data.x),int(state_data.y))
            t.write(j)
            guessed_state.append(j)
        else:
            continue
    i += 1
