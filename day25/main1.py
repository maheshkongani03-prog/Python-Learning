from turtle import Turtle,Screen
import pandas
screen=Screen()
screen.setup(750,550)
screen.bgpic("blank_states_img.gif")
data=pandas.read_csv("50_states.csv")
states=data.state.to_list()
is_on=True
while is_on:
    User_guess=screen.textinput("guess state name","Enter the state Name")
    for i in range(len(states)):
        if User_guess==states[i]:
            me=Turtle()
            me.hideturtle()
            me.penup()
            me.goto(data.User_guess.x,data.y[User_guess])
            me.write(User_guess)
screen.exitonclick()