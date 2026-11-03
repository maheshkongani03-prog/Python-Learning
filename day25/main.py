from turtle import Screen,Turtle
import pandas
screen=Screen()
screen.setup(750,500)
screen.bgpic("blank_states_img.gif")
data=pandas.read_csv("50_states.csv")
states_list=data.state.to_list()
print(len(states_list))
state="state"
missing_states=[]
guessed_states=[]
length=0
while length<50:
    answer=screen.textinput(f"{length}/50 states are correct",f"Enter the {state} Name:").title()

       
    if answer in states_list:
        guessed_states.append(answer)
        me=Turtle()
        me.hideturtle()
        me.penup()
        correct_guess=data[data.state==answer]
        state="another state"
        me.goto(correct_guess.x.item(),correct_guess.y.item())
        me.write(answer)
        length+=1
    elif answer=="Exit":
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
                length=51
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")


screen.exitonclick()
