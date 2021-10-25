import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = []
data = pandas.read_csv("50_states.csv")

state_list = data.state.to_list()
#coordinates = tuple(zip(states_data.x, states_data.y))


# for i in range(0, 49):
#     states_dict[state_list[i]] = coordinates[i]


def write_state(user_state):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == user_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(f"{user_state}")


while len(score) < 50:
    answer_state = screen.textinput(title=f"{len(score)}/50 States Correct", prompt="Enter a state's name").title()

    if answer_state.lower() == 'exit':
        missing_states = [state for state in state_list if state not in score]
        # for state in state_list:
        #     if state not in score:
        #         missing_states.append(state)
        print(missing_states)
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("missing_states.csv")
        break

    if answer_state in state_list:
        score.append(answer_state)
        write_state(answer_state)




# turtle.mainloop()
