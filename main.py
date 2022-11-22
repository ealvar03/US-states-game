import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
state_list = states_data["state"]

guessed_states = []
score = 0
length_guessed_states = len(guessed_states)
while length_guessed_states < 50:
    answer_state = screen.textinput(title=f"{score}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        data_dict = {
            "state to learn": missing_states
        }
        states_to_learn = pandas.DataFrame(data_dict)
        states_to_learn.to_csv("states_to_learn.csv")
        length_guessed_states = 50
        screen.bye()
    for state_name in state_list:
        state_coor = states_data[states_data.state == f"{state_name}"]

        if answer_state == state_name:
            guessed_states.append(state_name)
            state = turtle.Turtle()
            state.penup()
            state.hideturtle()
            state.goto(int(state_coor.x), int(state_coor.y))
            state.write(f"{state_name}")
            score += 1

