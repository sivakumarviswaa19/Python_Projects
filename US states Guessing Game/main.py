from turtle import Turtle,Screen
import pandas
screen=Screen()
turt=Turtle()
player=Turtle()
player.penup()
player.hideturtle()

screen.title("US States Game!")

bg="blank_states_img.gif"
screen.addshape(bg)
turt.shape(bg)

data = pandas.read_csv("50_states.csv")

is_game_on = True
score = 0
guessed_states = []
remaining = []

while is_game_on:
    guess = screen.textinput(f"{score}/50 Correct","Enter a States Name").title()
    states=data.state
    lis=states.tolist()
    if guess in lis and guess not in guessed_states:
        score += 1
        st_dt=data[data.state==guess]
        x=int(st_dt.x.item())
        y=int(st_dt.y.item())
        player.goto(x,y)
        player.write(f"{guess}",align="center",font=("Arial",10,"normal"))

    if score == 50:
        is_game_on=False
        player.goto(0,0)
        player.write("Congrats, YOU WON",align="center",font=("Courier",20,"normal"))

    if guess == "Exit":
        for i in lis:
            if i not in guessed_states:
                remaining.append(i)
        df=pandas.DataFrame(remaining)
        df.to_csv("remaining_states.csv")
        break


screen.exitonclick()