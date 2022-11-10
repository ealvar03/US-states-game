import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
title_state = answer_state.title()

states_data = pandas.read_csv("50_states.csv")
state_list = states_data["state"]
for state in state_list:
    if title_state == state:
        print("yes")

