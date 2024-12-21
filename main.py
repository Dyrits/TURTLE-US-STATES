import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.bgpic("states.image.gif")

states = pandas.read_csv("states.data.csv")

# Subtract 8 from each x value to readjust the position of the state name
states['x'] = states['x'] - 10

print(states[states["state"] == "Alabama"])

score = 0
found = []
prompt = "Welcome to the U.S. States Game! Guess the name of a state."
while score < 50:
    answer = screen.textinput(title="Guess the State", prompt=prompt)
    answer = answer.title()
    if answer == "Exit":
        break
    if states[states["state"] == answer].empty:
        prompt = f"{answer} is not a state! Try another guess."
    elif answer in found:
        prompt = "Not bad! But... you've already guessed that state! Try another one."
    else:
        found.append(answer)
        score += 1
        state = states[states["state"] == answer]
        # Write the name of the state on the map
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(int(state["x"]), int(state["y"]))
        text.write(answer)
        prompt = f"Good job! You've guessed {score} out of 50 states. Keep going! Guess another state."

if score == 50:
    screen.textinput(title="Guess the State", prompt="You've guessed all the states! Congratulations! Press OK to exit.")

screen.exitonclick()